import pytest     #checking testcase skipping 
import sys
def test_a1():
    assert 2!=3
@pytest.mark.skip("we are skipping this testcase")
def test_a2():
    assert 1

def test_a3():
    assert False

@pytest.mark.skipif(sys.version_info >(3,8), reason = "version should be less then 3.8")
def test_a4():
    assert True

def test_a5():
    assert 1 in divmod(9,5)
    assert 'viv' in 'vivek'