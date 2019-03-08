import pytest
class Test_abc:
    @pytest.mark.run(order = -1)
    def test_a(self):
        print("test_a")
        assert True

    @pytest.mark.run(order=1)
    def test_b(self):
        print("test_b")
        assert False
if __name__ == "__main__":
    pytest.main()