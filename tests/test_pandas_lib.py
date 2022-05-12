import pandas as pd
import pytest
from aft3000_lib.pandas_lib import pd_compare_datasets


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