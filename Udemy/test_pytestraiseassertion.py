import pytest
def test_case1():
    with pytest.raises(ZeroDivisionError):                 #with pytest.raises(Exception):
        assert (1/0)

def test_case0():
    raise ValueError("Exception func raised")
def test_case2():
    with pytest.raises(Exception) as errorinfo:
        assert 3==3
        test_case0()
        print(str(errorinfo) == "Exception func raised")