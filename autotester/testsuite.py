from autotester.common import *
from autotester.testcase import TestCase


class TestSuite:
    def __init__(self, name: str = 'testsuite') -> None:
        """
        测试套件类
        :param name: 测试套件的名称，用于测试用例的前缀
        """
        self.name = name
        self.dir_path = PATH_TB_DIR.joinpath(name)
        self.file_path = PATH_TB_DIR.joinpath(f'{name}.xlsx')
        self.testcases: List[TestCase]
        if self.file_path.exists():
            self.testcases = self._init_testcases(name)
        else:
            msg = '测试套件文件不存在'
            logger_error_debug(msg)
            raise EnvironmentError(msg)

    def _init_testcases(self, name: str = '') -> List:
        """
        从Excel文件生成TestCase对象列表
        :param name: 测试用例的前缀名称
        :return: 生成的TestCase对象列表
        """
        result = []
        data = tablib.Dataset().load(open(self.file_path, 'rb').read()).dict
        try:
            for row in data:
                tc = TestCase()
                tc.num = f'{name}_{row[TC_NUM]}'
                tc.title = row[TC_TITLE]
                tc.modules = row[TC_MODULES]
                tc.priority = str(row[TC_PRIORITY] or '')
                tc.preconditions = str(row[TC_PRECONDITIONS] or '')
                tc.steps = str(row[TC_STEPS] or '')
                tc.expected_results = str(row[TC_EXPECTED_RESULTS] or '')
                tc.remark = str(row[TC_REMARK] or '')
                tc.tag = str(row[TC_TAG] or '')
                result.append(tc)
        except Exception as e:
            logger_error_debug(f'生成测试用例对象列表异常：{e}')
        finally:
            return result

    def generate_file(self, new) -> bool:
        """
        生成测试套件文件
        :param new: 手工编写的测试用例文件路径
        :return: 生成成功与否
        """
        result = False
        try:
            auto_cols = [
                TC_NUM, TC_MODULES, TC_TITLE, TC_PRIORITY, TC_PRECONDITIONS,
                TC_STEPS, TC_EXPECTED_RESULTS, TC_REMARK, TC_TAG
            ]
            if self.file_path.exists():
                data = tablib.Dataset().load(open(self.file_path, 'rb').read())
                max_num = max([x[TC_NUM] for x in data.dict])
            else:
                data = tablib.Dataset()
                max_num = 0
                data.headers = auto_cols
            new_data = tablib.Dataset().load(open(new, 'rb').read()).dict
            while True:
                if len(new_data) == 0:
                    break
                new_row = new_data.pop(0)
                if new_row[TC_IS_AUTO] != TC_IS_AUTO_TRUE:
                    continue
                new_modules = new_row[TC_MODULES]
                new_title = new_row[TC_TITLE]
                for old_row in data.dict:
                    old_modules = old_row[TC_MODULES]
                    old_title = old_row[TC_TITLE]
                    if new_modules == old_modules and new_title == old_title:
                        new_row = None
                if new_row:
                    new_row = {x: new_row[x] for x in auto_cols}
                    new_row[TC_NUM] = max_num + 1
                    max_num += 1
                    new_list = [new_row[header] for header in data.headers]
                    data.append(new_list)
            with open(self.file_path, 'wb') as f:
                f.write(data.xlsx)
            result = True
        except Exception as e:
            logger_error_debug(f'生成自动化测试套件文件异常：{e}')
        finally:
            return result

    def generate_dir(self) -> bool:
        """
        生成测试用例脚本文件夹结构和测试用例脚本文件，内容为pass
        :return: 生成成功与否
        """
        result = False
        try:
            if not self.testcases:
                logger.warning('testcases为空，init_*方法未调用或者调用失败')
            else:
                template_path = Path.cwd().joinpath('autotester/template')
                for tc in self.testcases:
                    modules = tc.modules.split('/')[1:]
                    PATH_TB_DIR.joinpath('__init__.py').touch(exist_ok=True)

                    # 创建库文件夹
                    PATH_LIB_DIR.mkdir(exist_ok=True)
                    PATH_LIB_DIR.joinpath('__init__.py').touch(exist_ok=True)

                    # 创建公共库文件夹
                    PATH_LIB_DIR.joinpath('common').mkdir(exist_ok=True)
                    PATH_LIB_DIR.joinpath('common/__init__.py').touch(
                        exist_ok=True)

                    # 通过template文件生成py文件
                    for tpl in (template_path.iterdir()):
                        if tpl.is_file():
                            if 'testcase' in tpl.name:
                                continue
                            with tpl.open('r', encoding='utf-8') as f:
                                s = f.read()
                            if 'logger.template' in tpl.name:
                                s = s.replace('%level%', TC_LOG_FILE_LEVEL)
                                s = s.replace('%rotation%', TC_LOG_MAXBYTES)
                            dir_path = PATH_LIB_DIR.joinpath('common')
                            if 'init.template' in tpl.name:
                                file_name = '__init__'
                            else:
                                file_name = tpl.name.split('.')[0]
                            py_path = dir_path.joinpath(f'{file_name}.py')
                            with py_path.open('w', encoding='utf-8') as f:
                                f.write(s)

                    # 创建测试用例文件夹
                    dest_path = self.dir_path
                    dest_path.mkdir(exist_ok=True)
                    dest_path.joinpath('__init__.py').touch(exist_ok=True)

                    # 创建每层模块文件夹和__init__.py文件
                    for module in modules[:-1]:
                        dest_path /= module
                        dest_path.mkdir(exist_ok=True)
                        dest_path.joinpath('__init__.py').touch(exist_ok=True)

                    # 创建新测试用例文件
                    dest_path /= tc.get_filename()
                    if not dest_path.exists():
                        tc_tpl = (
                            template_path.joinpath('testcase.template.py'))
                        with tc_tpl.open('r', encoding='utf-8') as f:
                            s = f.read()
                        s = s.replace('/%modules%', '_'.join(modules))
                        with dest_path.open('w', encoding='utf-8') as f:
                            f.write(s)

                    # 在已存在的测试用例文件中增加测试用例函数
                    with dest_path.open('r', encoding='utf-8') as f:
                        s = f.read()
                        if f'def test_{tc.num}' in s:
                            logger.info(f'测试用例（{tc.num}）已存在，跳过生成')
                            continue
                    with dest_path.open('a', encoding='utf-8') as f:
                        f.write(tc.to_def())
                        logger.info(f'生成测试用例：{tc.num}')
                result = True
        except Exception as e:
            logger_error_debug(f'生成测试用例文件夹异常：{e}')
        finally:
            return result


if __name__ == "__main__":
    ts = TestSuite('动环盒子测试用例')
    # ts.generate_file(r'D:\奇迹智慧\Python\AutoTester\testbase\测试用例.xlsx')
    ts.generate_dir()
