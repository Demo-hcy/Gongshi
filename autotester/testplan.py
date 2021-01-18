from autotester.common import *
from autotester.testsuite import TestSuite
from autotester.testcase import TestCase
import shutil


class TestPlan:
    def __init__(self,
                 ts: TestSuite,
                 filter: Optional[Dict[str, List[str]]] = None,
                 library: Optional[List] = None) -> None:
        """
        测试计划类
        :param ts: 需进行测试计划的测试套件
        :param filter: 测试用例过滤器，默认为全部测试用例，可以配置{'功能模块': [],'标签': [],'优先级': []}
        :param library: 所需的库的名称列表（无需填写common库），默认为空列表，表示全部库
        """
        self.ts = ts
        self.filter = filter
        self.library = library
        self.testcase_list = self._select_tc()

    def _select_tc(self) -> List[TestCase]:
        tcs = [tc for tc in self.ts.testcases]
        tcs1 = []
        if '功能模块' in self.filter:
            for tc in tcs:
                for x in self.filter['功能模块']:
                    if set(x.split('/')) <= set(tc.modules.split('/')):
                        tcs1.append(tc)
                        break
            tcs = tcs1
            tcs1 = []
        if '标签' in self.filter:
            for tc in tcs:
                for x in self.filter['标签']:
                    if x in tc.tag.split(' | '):
                        tcs1.append(tc)
                        break
            tcs = tcs1
            tcs1 = []
        if '优先级' in self.filter:
            for tc in tcs:
                for x in self.filter['优先级']:
                    if x == tc.priority:
                        tcs1.append(tc)
                        break
            tcs = tcs1
            # tcs1 = []
        pprint(tcs)
        # tcs = [self.ts.path.joinpath(tc.get_path()) for tc in tcs]
        return tcs

    def generate(self, name: str) -> None:
        if name:
            path = PATH_PLAN_DIR.joinpath(name)
            path.mkdir(exist_ok=True)

            lib_path = path.joinpath('library')
            lib_path.mkdir(exist_ok=True)
            lib_path.joinpath('__init__.py').touch(exist_ok=True)

            common_path = lib_path.joinpath('common')
            common_path.mkdir(exist_ok=True)
            common_path.joinpath('__init__.py').touch(exist_ok=True)

            tc_path = path.joinpath('testcase')
            tc_path.mkdir(exist_ok=True)
            tc_path.joinpath('__init__.py').touch(exist_ok=True)

            log_path = path.joinpath('testlog')
            log_path.mkdir(exist_ok=True)

            public_var_path = path.joinpath('public_var')
            public_var_path.mkdir(exist_ok=True)
            shutil.copy(PATH_TB_DIR.joinpath('public_var/public_enum.py'),
                        public_var_path.joinpath('public_enum.py'))

            public_method_path = path.joinpath('public_method')
            public_method_path.mkdir(exist_ok=True)

            # 添加common库到库列表
            lib_list = self.library
            lib_list.append('common')

            # 复制库
            for sub_lib in lib_list:
                sub_lib_path = lib_path.joinpath(sub_lib)
                sub_lib_path.mkdir(exist_ok=True)
                src = PATH_LIB_DIR.joinpath(sub_lib)
                copy_dir(src, sub_lib_path)

            # 复制测试用例目录结构
            copy_dir(self.ts.dir_path, tc_path, True, True)

            # 复制测试用例
            tc_set = set([
                self.ts.dir_path.joinpath(tc.get_path())
                for tc in self.testcase_list
            ])
            for tc in tc_set:
                tc_new = str(tc).replace(str(self.ts.dir_path) + '\\', '')
                tc_new = tc_path.joinpath(tc_new)
                shutil.copy(tc, tc_new)
                with open(tc_new, 'r', encoding='utf-8') as f:
                    s = f.read()
                s_new = []
                for case in s.split('@allure'):
                    if 'severity' in case:
                        for x in self.testcase_list:
                            if (x.title in case) and (x.modules in case):
                                s_new.append(case)
                    else:
                        s_new.append(case)
                s_new = '@allure'.join(s_new)
                with open(tc_new, 'w', encoding='utf-8') as f:
                    f.write(s_new)

    # def run(self) -> None:
    #     """
    #     按测试计划执行测试用例
    #     :param plan: 待执行的测试计划
    #     """
    #     pprint(self.testcase_list)
    #     tc_list = [str(x) for x in self.testcase_list]
    #     tc_list.append(f'--alluredir={PATH_REPORT_DIR}\\allure-results')
    #     tc_list.append('--clean-alluredir')
    #     tc_list.append('-v')
    #     tc_list.append('-s')
    #     os.chdir(PATH_TS_DIR)
    #     sys.path.append(str(PATH_TS_DIR))
    #     pytest.main(tc_list)
    # os.system('allure serve {}'.format(PATH_REPORT_DIR))
    # os.system('allure generate -c {}\\allure-results -o {}\\allure-report'.
    #           format(PATH_REPORT_DIR, PATH_REPORT_DIR))
    # os.system('allure open {}\\allure-report'.format(PATH_REPORT_DIR))


if __name__ == "__main__":
    ts = TestSuite('testsuite1')
    fileter = {'功能模块': ['/手动控制广播/添加节目'], '标签': ['冒烟测试', '集成测试'], '优先级': ['高']}
    tp = TestPlan(ts, fileter, ['mqtt_lib'])
    tp.generate('tp1')
