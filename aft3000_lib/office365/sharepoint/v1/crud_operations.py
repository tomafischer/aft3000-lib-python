from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential

import json
import pandas as pd

def sp_connect_app_principal(app_principal: dict, site_url: str) -> ClientContext:
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

def sp_get_list_items(ctx, list_name: str, filter_query = None, print_progress = sp_print_progress):
    list_object = ctx.web.lists.get_by_title(list_name)

    #adding paging for longer lists
    items = list_object.items.paged(True)
    ## add progress status
    if print_progress:
        items.page_loaded += print_progress
    if filter_query:
        items.filter(filter_query)
    #loading the items
    ctx.load(items)
    ctx.execute_query()
    # getting response
    print(f"Loaded items count: {len(items)}")
    #for item in items:
        # pass
        #print(type(item.properties))
        #print(f"{item.properties}")
    return items #, list_object

# adding items
def sp_add_item(ctx, list_name, item_dict, verbose= True):
    list_object = ctx.web.lists.get_by_title(list_name)
    sp_item = list_object.add_item(item_dict).execute_query()
    if verbose:
        print(f"Item created with SharePoint_Id: {sp_item.id}")
    return sp_item

def sp_recycle_item(ctx, item_id, target_list):
    #https://github.com/vgrem/Office365-REST-Python-Client/blob/master/examples/sharepoint/listitems/delete_list_item.py
    #target_list = ctx.web.lists.get_by_title(list_name)
    #item_id = items[0].id
    target_list.get_item_by_id(item_id).recycle().execute_query()


def sp_list_items_2_pd(list_items):
    """"
   Converting Sharepoint List items to pandas 
    """
    all= list(list_items)
    all = [i.properties for i in all]
    all_json = json.dumps(all)
    all_pd = pd.read_json(all_json)

    return all_pd