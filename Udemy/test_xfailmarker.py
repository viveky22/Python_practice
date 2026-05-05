import pytest
import sys                 #py.test -v -s -k "case"    - Important
def test_1():
    a = 'vivek'
    assert a[1] == 'i'

def test_2():
    b = 'yadav'
    assert b[0] == 'y'

@pytest.mark.xfail(sys.platform == 'win32', reason = 'this should be run in win32')
def test_3():
    c = 'uttar' + 'pradesh'
    assert c == 'uttarprades'
