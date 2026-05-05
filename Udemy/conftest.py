import pytest
import os

QA_config = 'qa.prop'
prod_config = 'prof.prop'


def pytest_addoption(parser):
    parser.addoption("--cmdopt", default = 'QA')

@pytest.fixture()
def CmdOpt(pytestconfig):
    print("\n  this is pytest fixture \n")
    opt = pytestconfig.getoption('cmdopt')
    if opt == 'prod':
        f = open(os.path.join(os.path.dirname(__file__),prod_config), 'r')
    else:
        f = open(os.path.join(os.path.dirname(__file__),QA_config), 'r')
    yield f