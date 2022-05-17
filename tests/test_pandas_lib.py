import pandas as pd
import pytest
from aft3000_lib.pandas_lib import pd_compare_datasets, pd_str_to_DT, pd_DT_to_str
from datetime import datetime

_original = pd.DataFrame([[1,2,"test"], [2,3,"me"]], columns=['A', 'B', 'C'])
_compare = pd.DataFrame([[1,2,"test"], [4,3,"me"]], columns=['A', 'B', 'C'])

@pytest.fixture
def original_pd():
    return _original

@pytest.fixture
def compare_pd():
    return _compare

@pytest.mark.pd
def test_compare_datasets(original_pd, compare_pd):
    ret =  pd_compare_datasets(original_pd=original_pd, compare_pd=compare_pd, on=['A','B'], compare_column='C', suffixes=['_one','_two'])
    assert 'C_one' in ret['added'].columns , "check if column names were correctly added"
    assert 'C_two' in ret['added'].columns
    assert len(ret['added']) ==1 
    assert len(ret['del']) == 1
    assert ret['added'].iloc[0,0] == 4
    assert ret['del'].iloc[0,0] == 2
    return ret

@pytest.mark.pd
def test_pd_str_to_DT():
    # arrange
    data_pd = pd.DataFrame([["2022-03-21 01:15:22.123456", "2022-03-22 01:15:22"],["",""]], columns=["dt1", "dt2"])
    # act
    t = pd_str_to_DT(data_pd=data_pd, columns=['dt1', 'dt2'])
    assert t.iloc[0]['dt1'] == datetime(2022,3,21,1,15,22,123456)
    assert t.iloc[0]['dt2'] == datetime(2022,3,22,1,15,22)
    assert pd.isnull(t.iloc[1]['dt1']), 'Check if we have NaT'
    return data_pd, t

# @pytest.mark.pd
# def test_pd_DT_to_str():
#     # arrange
#     data_pd = pd.DataFrame([[datetime(2022,3,21,1,15,22,123456), datetime(2022,3,22,1,15,22)],["",""]], columns=["dt1", "dt2"])
#     # act
#     t = pd_DT_to_str(data_pd=data_pd)
#     assert t.iloc[0]['dt1'] == datetime(2022,3,21,1,15,22,123456)
#     assert t.iloc[0]['dt2'] == datetime(2022,3,21,1,15,22)
#     assert pd.isnull(t.iloc[1]['dt1']), 'Check if we have NaT'
#     return data_pd, t