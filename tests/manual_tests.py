from cmath import isnan
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

# sp_remove_columns_manul()

###
#  Pandas tests
###
from aft3000_lib.pandas_lib import pd_compare_datasets, pd_str_to_DT
from aft3000_lib.pandas_lib import pd_DT_to_str
from tests.test_pandas_lib import test_compare_datasets
from tests.test_pandas_lib import _compare, _original
original_pd = pd.DataFrame([[1,2,"test"], [2,3,"me"]], columns=['A', 'B', 'C'])
compare_pd = pd.DataFrame([[1,2,"test2"], [4,3,"me2"]], columns=['A', 'B', 'C'])
#ret = test_compare_datasets(_original, _compare)


data_pd = pd.DataFrame([["2022-03-21 01:15:22.123456", "2022-03-22 01:15:22"],["",""]], columns=["dt1", "dt2"])
t = pd_str_to_DT(data_pd=data_pd, columns= ['dt1', 'dt2'])
#def pd_str_to_DT():

data_pd = pd.DataFrame([[datetime(2022,3,21,1,15,22,123456), datetime(2022,3,22,1,15,22)],["",""]], columns=["dt1", "dt2"])
# act
pd.core.dtypes.common.is_datetime_or_timedelta_dtype(data_pd['dt1'])
t2 = pd_DT_to_str(data_pd=data_pd, verbose= True, replace_NaN_str="")

col = 'dt1'
replace_NaN_str = 'dude'
t2.apply(lambda x: replace_NaN_str if pd.isnull(x[col]) else x[col], axis=1)