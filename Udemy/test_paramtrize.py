import pytest

@pytest.mark.parametrize('a', [4,5,2,7,1,8,9])   #py.test test_paramtrize.py -v -s --tb=no
def test_a(a):
    assert a>4

@pytest.mark.parametrize('a, out', [(2,4),(3,27)])
def test_b(a,out):
    assert (a**a)  == out