import pytest
@pytest.fixture()
def init_xx():
    print("init sqlconnector")
    with open("./file/data.txt","w") as f:
        f.write("xxx,test")
@pytest.mark.usefixtures("init_xx")
class Test_xx:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_xx(self):
        print("test_xx")
        with open("./file/data.txt","rb") as f:
            data=f.read()
            with open("./file/copy.txt","w") as w:
                w.write(data)
            with open("./file/copy.txt","r") as X:
                #assert f.read() == X.read(), 'copy error' #f.read()=''
                assert data == X.read(), 'copy error'
    def test_yy(self):
        assert True


