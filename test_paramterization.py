import pytest

@pytest.fixture
def dataload():
    return ["Vivek", "Python", "Automation"]


def test_para(dataload):
    print("Taking data from fixture")
    print(dataload)

#it is a feature that allows a single test features to be run with multiple set of input data, 
# eliminating the need to repitatice test code