import pytest
@pytest.fixture(scope='function',autouse=True,params=[3,4,5,6])
def init_xx(request):
    print(request.param)
    print(">>>>>before")
@pytest.mark.usefixtures("init_xx")
class Test_xx:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_xx(self):
        assert init_xx == 4
    def test_yy(self):
        assert init_xx == 5


