import sys
import pytest
from mock import patch
from weather import Weather


@pytest.fixture
def single_city():
    '''Returns no argument'''
    return 'London'

def test_parse_args_pass(single_city):
    testargs = [__name__, single_city]
    with patch.object(sys, 'argv', testargs):
        location = Weather.get_location()
        assert location == single_city

def test_parse_args_fail():
    testargs = [__name__]
    with patch.object(sys, 'argv', testargs):
        with pytest.raises(SystemExit):
            Weather.get_location()
        #optionally we could test output before sys.exit running pytest with --capture=sys option
        #https://stackoverflow.com/questions/30256332/verify-the-the-error-code-or-message-from-systemexit-in-pytest