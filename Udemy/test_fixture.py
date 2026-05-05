import pytest

@pytest.fixture()
def setup_list():
    print("\n we are in fixture \n")
    city = ['bangalore','delhi','pune','kanpur']
    return city

def test_getcity(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'bangalore'
    assert setup_list[-1] == 'kanpur'

def myreverse(lst):
    lst.reverse()
    return lst

def test_reverselist(setup_list):
    assert setup_list[::-1] == myreverse(setup_list)

#@pytest.mark.xfail(reason="expected failure")
@pytest.mark.usefixtures("setup_list")
def test_usefixturedemo():
    assert 1 == 1
    assert setup_list[0] == 'bangalore'

filename  = 'file1.txt'

@pytest.fixture()
def setup_03():
    f = open(filename,'w')
    f.write("pytest is good")
    f.close()
    f = open(filename,'r+')
    yield f

def test_filetest(setup_03):
    assert (setup_03.readline())  == "pytest is good"