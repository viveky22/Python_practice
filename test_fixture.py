import pytest

@pytest.fixture()
def setup():
    print("i'll execute first")
    yield
    print("i'll execute at last")

def test_fixturedemo(setup):
    print("im the test case")

    