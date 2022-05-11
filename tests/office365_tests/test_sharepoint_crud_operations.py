
from aft3000_lib.office365.sharepoint.v1.crud_operations import sp_connect_app_principal, sp_get_list_object, sp_getWebsiteTitle, sp_get_list_items, sp_add_item, sp_recycle_item, sp_list_items_2_pd, sp_remove_sharepoint_columns
import pytest

import uuid


"""
Arrange
"""


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

@pytest.mark.sp
def test_sp_list_items_2_pd(ctx, list_name):
    items_sp = sp_get_list_items(ctx, list_name) 
    items_pd = sp_list_items_2_pd(list_items= items_sp)     
    items_clean = sp_remove_sharepoint_columns(items_pd)
    assert len(items_pd.columns) == len(items_clean.columns) , "Columns should be the same, due that the header was already removed" 

@pytest.mark.sp
def test_sp_list_items_2_pd_no_removed(ctx, list_name):
    items_sp = sp_get_list_items(ctx, list_name) 
    items_pd = sp_list_items_2_pd(list_items= items_sp, remove_sp_columns= False)     
    items_clean = sp_remove_sharepoint_columns(items_pd)
    assert len(items_pd.columns) != len(items_clean.columns) , "Columns should be different" 


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





