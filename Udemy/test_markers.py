import pytest

@pytest.mark.sanity
def test_01():
    num = 9/4
    s1 = 'i like ' + 'pytest automation'
    assert str(num) == '2.5'
    assert s1 == 'i like pytest automation'

def test_02():
    letter = 'vivek'
    assert len(letter) == 5

@pytest.mark.sanity
@pytest.mark.str
def test_03():
    a = 'yadav'
    assert a[0] == 'y'

def test_04():
    b = 'vivekyadav'
    assert b[:] == 'vivekyadav'
    assert b[-1] == 'v'