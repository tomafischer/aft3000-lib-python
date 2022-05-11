import pytest

_app_principal = {    
    'client_id': '',
    'client_secret': '',
    }
_site_url = "https://mecloud.sharepoint.com/teams/mysite"

_list_name = "Unittests"

@pytest.fixture
def app_principal():
    print("app_principal loaded")
    yield _app_principal
    print("app_principal finalized")

@pytest.fixture
def site_url():
    return _site_url

@pytest.fixture
def list_name():
    return _list_name