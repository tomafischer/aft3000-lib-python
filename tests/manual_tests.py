import os 
from datetime import datetime
import pandas as pd
os.chdir('../')


from tests.conftest import _app_principal, _site_url, _list_name
from aft3000_lib.office365.sharepoint.v1.crud_operations import sp_connect_app_principal, sp_get_list_items, sp_list_items_2_pd, sp_remove_sharepoint_columns, sp_list_items_2_pd

print(os.getcwd())

def sp_sharepoint_manual():
    _ctx = sp_connect_app_principal(_app_principal, _site_url)
    items = sp_get_list_items(_ctx, _list_name)
    for i in items:
        print(i.properties)
    return items
def sp_remove_columns_manul():
    items_sp = sp_sharepoint_manual()  
    items_pd = sp_list_items_2_pd(list_items= items_sp)     
    items_clean = sp_remove_sharepoint_columns(items_pd)
    print(items_clean.info())

sp_remove_columns_manul()