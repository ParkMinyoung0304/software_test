# 理解pytest的框架架构setup和teardown
import pytest

#python中一个模块就是一个文件，setup_module整个模块中只执行一次
def setup_module():
    print("\n￥￥￥￥￥setup_module:整个模块开始只执行一次￥￥￥￥￥")
def teardown_module():
    print("\n￥￥￥￥￥teardown_module:整个模块结束只执行一次￥￥￥￥￥")

# 类外测试用例
def setup_function():
        print("**setup_function:每个不在类中的用例开始前都会执行")
def teardown_function():
        print("**teardown_function:每个不在类中的用例结束后都会执行")
def test_one():
    print("正在执行测试模块：test one")
def test_two():
    print("正在执行测试模块：test two")

# 测试类
class TestCase():
    def setup_class(self):
        print("\n**setup_class:class类里面所有用例执行前执行 1")#执行一次
    def teardown_class(self):
        print("\n**teardown_class:class类里面所有用例执行后执行 2")#执行一次
    def setup(self):
        print("\nsetup:每个用例开始前都会执行 3")#有几个用例执行几次
    def teardown(self):
        print("\nteardown:每个用例结束后执行 4")#有几个用例执行几次
    def  test_three(self):
        print("\n正在执行测试模块：test three 5")
    def  test_four(self): 
        print("\n正在执行测试模块：test four 6")







