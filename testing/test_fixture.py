import pytest


@pytest.fixture(scope="module",params=[
    [1,1,2],
    [2,1,3]
])
def data(request):
    print("这是1")
    yield  request.param

class TestFixture:
    def test_add(self):
        assert  1+1 == 2

    def test_add2(self, data):
        print("这是2")
        assert  data[0]+ data[1] == data[2]

    @pytest.mark.parametrize("data", [
    [1,1,2],
    [2,1,3]
    ])
    def test_add3(self, data):
        assert data[0] + data[1] == data[2]

    def provider(self):
        for i in range(5):
            # yield i
            return i
            print("after yiel")

    def test_provider(self):
        for d in self.provider():
            print(f"d是：{d}")

    def test_wont(self):
        a=3
        b=4
        a,b=b,a+b
        print(a)
        print(b)
