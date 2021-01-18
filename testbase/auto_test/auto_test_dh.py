import pytest

args = []
args.append('-s')  # 输出打印信息
args.append('-v')  # 输出详细信息
args.append('-x')  # 出现一条测试用例失败就退出测试
args.append('动环盒子测试用例/属性功能/test_485通宵配置消息.py::test_动环盒子测试用例_181')
pytest.main(args)
