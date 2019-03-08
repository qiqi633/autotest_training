import pytest
@pytest.fixture(scope='function',autouse=True)
def init_xx():
    print(">>>>>before")
@pytest.mark.usefixtures("init_xx")
class Test_xx:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_xx(self):
        print(">>>>>test_xx")
    def test_yy(self):
        print(">>>>>test_yy")


