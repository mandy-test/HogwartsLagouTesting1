#pytest 先去执行这个文件下的
from _pytest.main import Session


def pytest_collection_modifyitems(session: Session, config, items: list):
    items.reverse()
    session.items=items

class Calc:
    def add(self, a, b) -> int:
        print(a)
        print(b)
        return a + b
    def add2(self, a, b) -> int:
        print(a)
        print(b)
        return a + b

    def div(self, a, b):
        return a / b