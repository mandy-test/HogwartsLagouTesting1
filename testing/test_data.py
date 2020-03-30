import pytest
import yaml

def data():
    with open("testing/test_data.yaml") as f:
        return yaml.load(f)

class TestCalc:

    @pytest.mark.parametrize("a,b ,r", data())
    def test_params(self, a,b,r):
        print("param")
        data=(a,b)
        assert  self.Calc.add2(data) == r
        self.Calc.add2(*data)

    def steps(self, data, r):
        test_steps = steps()
        for step in test_steps:
            if step == "add":
                self.Calc.add(data)
            elif step == "add2":
                self.Calc.add2(data)

