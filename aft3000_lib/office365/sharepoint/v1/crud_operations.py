from xmlrpc.client import Boolean
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential

import json
import pandas as pd

def sp_connect_app_principal(app_principal: dict, site_url: str) -> ClientContext:
    """
    Uses an application Id to authenticate agains Sharepoint online. Works with MFA.
    For details see:
    https://code2care.org/sharepoint/how-to-access-sharepoint-online-data-using-postman-rest-graph-api-oauth
    """
    credentials = ClientCredential(app_principal['client_id'], app_principal['client_secret'])
    ctx = ClientContext(site_url).with_credentials(credentials)
    return ctx

def sp_getWebsiteTitle(ctx, verbose = True):
    web = ctx.web
    ctx.load(web)
    ctx.execute_query()
    if verbose:
        print("Web site title: {0}".format(web.properties['Title']))
    return web.properties['Title']

def sp_print_progress(items_read):
    print("Items read: {0}".format(items_read))

def sp_get_list_object(ctx, list_name):
    return ctx.web.lists.get_by_title(list_name)

def sp_get_list_items(ctx, list_name: str, filter_query = None, print_progress = sp_print_progress, verbose: Boolean= True):
    """
    Retrieve List items from list_name
    Filter example: fitler_query = "System_Type eq 'Sales' and Deparment eq 'Internet'"
    """
    list_object = ctx.web.lists.get_by_title(list_name)

    #adding paging for longer lists
    items = list_object.items.paged(True)
    ## add progress status
    if print_progress and verbose:
        items.page_loaded += print_progress
    if filter_query:
        items.filter(filter_query)
    #loading the items
    ctx.load(items)
    ctx.execute_query()
    # getting response
    if verbose:
        print(f"Loaded items count: {len(items)}")
    #for item in items:
        # pass
        #print(type(item.properties))
        #print(f"{item.properties}")
    return items #, list_object

# adding items
def sp_add_item(ctx, list_name, item_dict, verbose= True):
    """
    Adding items to Sharepoint. 
    """
    list_object = ctx.web.lists.get_by_title(list_name)
    sp_item = list_object.add_item(item_dict).execute_query()
    if verbose:
        print(f"Item created with SharePoint_Id: {sp_item.id}")
    return sp_item

def sp_get_target_list(ctx, list_name: str):
    """
    Get target_list object. Can be reused for sp_recycle_item
    """
    return ctx.web.lists.get_by_title(list_name)

def sp_recycle_item(item_id, target_list):
    """
    Recycles the item on the target_list.
    Call sp_get_target_list to retrieve the target_list obejct by name
    
    For details see:
    https://github.com/vgrem/Office365-REST-Python-Client/blob/master/examples/sharepoint/listitems/delete_list_item.py
    
    Example for getting the iteme id from a sharepont item:
    item_id = items[0].id
    """
    target_list.get_item_by_id(item_id).recycle().execute_query()


def sp_remove_sharepoint_columns(data_pd: pd, verbose= False) -> pd:
    """
    Remove all extra columns from Sharepoint. 
    If columns are already removed we skip those columns
    """
    for h in [ "Id", "ID", "FileSystemObjectType","ServerRedirectedEmbedUri", "ServerRedirectedEmbedUrl","ContentTypeId","Modified","Created","AuthorId","EditorId", "OData__UIVersionString","Attachments","GUID", "ComplianceAssetId"]:
        if h in data_pd.columns:
            data_pd = data_pd.drop(columns=[h])
    return data_pd

def sp_list_items_2_pd(list_items, remove_sp_columns = True, verbose= False):
    """"
    Converting Sharepoint List items to pandas 
    """
    all= list(list_items)
    all = [i.properties for i in all]
    all_json = json.dumps(all)
    all_pd = pd.read_json(all_json)

    if remove_sp_columns:
        if verbose:
            print("Remove Sharepoint Columns")
        all_pd = sp_remove_sharepoint_columns(data_pd=all_pd)
    return all_pd