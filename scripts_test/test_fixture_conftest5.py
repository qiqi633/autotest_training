import pytest
class Test_xx:
    def setup_class(self):
        print("setup_class")
    def teardown_class(self):
        print("teardown_class")
    def test_xx(self,init_conf):
        print("xx us conftest param[%s]",init_conf)
    def test_yy(self,init_conf):
        print("yy us conftest param[%s]",init_conf)


