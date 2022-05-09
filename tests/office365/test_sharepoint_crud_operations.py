
from aft3000_lib.office365.sharepoint.v1.crud_operations import sp_connect_app_principal, sp_get_list_object, sp_getWebsiteTitle, sp_get_list_items, sp_add_item, sp_recycle_item
import pytest

import uuid
"""
sharepoint settings
"""
_app_principal = {    
    'client_id': '',
    'client_secret': '',
    }
_site_url = 'https://my.sharepoint.com/teams/test'



_list_name = "Unittests"
"""
Arrange
"""

@pytest.fixture
def app_principal():
    return _app_principal
@pytest.fixture
def site_url():
 return _site_url

@pytest.fixture
def list_name():
    return _list_name

@pytest.fixture
def ctx(app_principal,site_url):
    return sp_connect_app_principal(app_principal, site_url)


"""
Act, Assert
"""
@pytest.mark.sp
@pytest.mark.tryfirst
def test_sp_connect_app_principal(app_principal, site_url):
    ctx = sp_connect_app_principal(app_principal, site_url)
    assert ctx is not None

@pytest.mark.sp
def test_sp_getWebsiteTitle(ctx):
    title = sp_getWebsiteTitle(ctx)
    assert bool(title) is True 

@pytest.mark.sp
def test_sp_get_list_items___no_filters(ctx, list_name):
    items = sp_get_list_items(ctx, list_name)
    assert len(items) >= 0
    # in case we have records check the first title
    if len(items) > 0:
        title = list(items)[0].properties['Title'] 
        assert bool(title) is True

@pytest.mark.skip
@pytest.mark.integration
def test_sp_get_list_items___crud_filters(ctx, list_name):
    """
    This is an integration test. uncomment the skip attri
    """
    #random title
    title = f"UnitTest {str(uuid.uuid4())}"
    print(f"Title: {title}")
    #adding item
    for i in range(2):
        item = {"Title": title}
        sp_add_item(ctx,list_name, item)
    
    #getting items
    filter_query = f"Title eq '{title}'"
    items = sp_get_list_items(ctx, list_name, filter_query=filter_query)
    assert len(items) == 2

    # deleteing items
    target_list = sp_get_list_object(ctx, list_name)
    for item in items:
        sp_recycle_item(ctx, item.id, target_list=target_list)



####
#   Manual tests can be run in interactive console
####
#os.chdir('../')
def manual():
    _ctx = sp_connect_app_principal(_app_principal, _site_url)
    items = sp_get_list_items(_ctx, _list_name)
    for i in items:
        print(i.properties)