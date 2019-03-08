import pytest

def re_data_list():
    list_data=[]
    with open('../file/parmetrize_data.txt','r') as f:
        for i in f.readlines():
            #split ,eval
            list_data.append(eval(i.split("=")[-1]))
        print(list_data)
        return list_data

class Test_parametrize:
    def setup_class(self):
        print("\\n>>>>>>>> setup")
    def teardown_class(self):
        print(">>>>>>>> teardown")
    @pytest.mark.parametrize("a",[3,4])
    def test_aa(self,a):
        print("param is %s",a)
        assert True
    @pytest.mark.parametrize("li,wang",re_data_list())
    def test_bb(self,li,wang):
        print("param is %s,%s",li,wang)
        assert True