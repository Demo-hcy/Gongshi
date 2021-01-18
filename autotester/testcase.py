from autotester.common import *


class TestCase:
    def __init__(self,
                 num: str = '',
                 title: str = '',
                 modules: str = '',
                 priority: str = '',
                 preconditions: str = '',
                 steps: str = '',
                 expected_results: str = '',
                 remark: str = '',
                 tag: str = '') -> None:
        """
        测试用例类
        :param num: 用例编号
        :param title: 用例标题
        :param modules: 功能模块
        :param priority: 优先级
        :param preconditions: 前置条件
        :param steps: 步骤描述
        :param expected_results: 预期结果
        :param remark: 备注
        :param tag: 标签
        """
        self.num = num
        self.title = title
        self.modules = modules
        self.priority = priority
        self.preconditions = preconditions
        self.steps = steps
        self.expected_results = expected_results
        self.remark = remark
        self.tag = tag

    def __repr__(self) -> str:
        result = (self.num, self.title, self.modules, self.priority,
                  self.preconditions, self.steps, self.expected_results,
                  self.remark, self.tag)
        return repr(result)

    def to_def(self) -> str:
        """
        生成测试用例脚本文件def基本结构和注解内容的字符串
        :return: 字符串
        """
        priority = {'高': 'CRITICAL', '中': 'NORMAL', '低': 'MINOR'}
        case = f'@allure.severity(allure.severity_level.{priority[self.priority]})\n'
        case += f'def test_{self.num}():\n'
        case += '    """\n'
        case += f'    - 用例标题：{self.title}\n'
        case += f'    - 功能模块：{self.modules}\n'
        case += f'    - 优先级：{self.priority}\n'
        case += f'    - 前置条件：\n{align_line(self.preconditions)}\n'
        case += f'    - 步骤描述：\n{align_line(self.steps)}\n'
        case += f'    - 预期结果：\n{align_line(self.expected_results)}\n'
        case += f'    - 备注：\n{align_line(self.remark)}\n'
        case += f'    - 标签：\n{align_line(self.tag)}\n'
        case += '    """\n'
        case += '    pass\n'
        case += '\n\n'
        return case

    def get_filename(self):
        return 'test_' + self.modules.split('/')[-1] + '.py'

    def get_path(self):
        p = Path()
        module_list = self.modules.split('/')
        for module in module_list[:-1]:
            p /= module
        p /= self.get_filename()
        return p
