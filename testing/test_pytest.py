import sys

from python.calc import Calc

sys.path.append("..")

#
# def teardown_class():
#     print("teardown_method")
"""
控制环境初始化
"""
def setup_module(self):
    print("setup_module")

def teardown_module(self):
    print("teardown_module")

class TestCalc:
    #类初始化执行一次
    @classmethod
    def setup_class(cls):
        print("setup_class")

    def setup_method(self):
        print("setup_method")

    def setup(self):
        self.calc = Calc()
        print("setup")

    def test_add(self):
        assert self.calc.add(1, 2) == 3

    def test_div(self):
        assert self.calc.div(1, 2) == 0.5

    def test_paras(self):
        data = {"a": 1, "b": 2}
        # self.calc.add2(data)
        self.calc.add(**data)

    def teardown(self):
        print("teardown")


    def teardown_method(self):
        print("teardown_method")


    def teardown_class(self):
        print("teardown_class")

