import pytest

@pytest.fixture()
def setup():
    print("i'll execute first")
    yield
    print("i'll execute at last")



@pytest.fixture()
def dataload():
    print("parameterization data load is here")
    return ["vivek", "yadav"]

    