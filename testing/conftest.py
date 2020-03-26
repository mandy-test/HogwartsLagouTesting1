#pytest 先去执行这个文件下的
from _pytest.main import Session


def pytest_collection_modifyitems(session: Session, config, items: list):
    items.reverse()
    session.items=items