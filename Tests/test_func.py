import pytest
from func_sample import fun, fun_exception

# configuring pytest in pycharm
# http://gowrishankarnath.com/using-pytest-testing-tool-to-test-python-code-by-configuring-pycharm-ide/

def test_answer():
    '''Testing function if return expected value'''
    assert fun(3) == 4
    with pytest.raises(ValueError):
        fun('xxx')

def test_mytest():
    '''Testing function that raises SystemExit exception.'''
    with pytest.raises(SystemExit):
        fun_exception()
