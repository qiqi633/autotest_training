import pytest
def check_4():
    list = [1,2,3,4,5]
    if 4 in list:
        return True
    else:
        return False
class Test_Pas:
    data=check_4()

    @pytest.mark.xfail(data, reason="4 is in the list ,so skip test_a")
    def test_a(self):
        print ("False")
        assert False


    def test_b(self):
        print("True")
        assert True
