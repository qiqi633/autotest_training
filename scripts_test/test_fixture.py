import pytest
@pytest.fixture()
def init_xx():
    print("init sqlconnector")
    with open("./file/data.txt","w") as f:
        f.write("xxx,test")

class Test_xx:
    def test_xx(self,init_xx):
        print("test_xx")
        with open("./file/data.txt","rb") as f:
            data=f.read()
            with open("./file/copy.txt","w") as w:
                w.write(data)
            with open("./file/copy.txt","r") as X:
                #assert f.read() == X.read(), 'copy error' #f.read()=''
                assert data == X.read(), 'copy error'

