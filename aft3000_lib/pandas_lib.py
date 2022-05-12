import pandas as pd

def pd_compare_datasets(original_pd: pd, compare_pd: pd, on : list,  compare_column: str, suffixes=['_o','_c'] ) -> pd:
    """
    Compares two pandas datasets and returns added/deleted records
    """
    diff_added = pd.merge(original_pd,compare_pd, how="right", on =on,suffixes= ['_o','_c'])
    diff_added = diff_added[diff_added[f'{compare_column}{suffixes[0]}'].isnull()]
    diff_del = pd.merge(original_pd,compare_pd, how="left", on = on,suffixes= ['_o','_c'])
    diff_del = diff_del[diff_del[f'{compare_column}{suffixes[1]}'].isnull()]
    return { 
        'added': diff_added,
        'del': diff_del
        }