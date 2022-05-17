import pandas as pd

def pd_compare_datasets(original_pd: pd, compare_pd: pd, on : list,  compare_column: str, suffixes=['_o','_c'] ) -> pd:
    """
    Compares two pandas datasets and returns added/deleted records
    """
    diff_added = pd.merge(original_pd,compare_pd, how="right", on =on,suffixes= suffixes)
    diff_added = diff_added[diff_added[f'{compare_column}{suffixes[0]}'].isnull()]
    diff_del = pd.merge(original_pd,compare_pd, how="left", on = on,suffixes= suffixes)
    diff_del = diff_del[diff_del[f'{compare_column}{suffixes[1]}'].isnull()]
    return { 
        'added': diff_added,
        'del': diff_del
        }

def pd_str_to_DT(data_pd:pd, columns: list, format: str = "%Y-%m-%d %H:%M:%S") -> pd:
    """
    Converts a string to a timestamp
    This default format also works with attached ms as long as a dot is used: 2022-03-21 01:15:22.123456
    
    other examples for format with ns: "%Y-%m-%d %H:%M:%S:%f"
    actual code: items_pd["Start"] = pd.to_datetime(items_pd["Start"], format= "%Y-%m-%d %H:%M:%S", errors='coerce')
    """
    for col in columns:
       data_pd[col] = pd.to_datetime(data_pd[col],format= format,errors='coerce')
    return data_pd

def pd_DT_to_str(data_pd: pd, columns:list = [], format="%Y-%m-%d %H:%M:%S", replace_NaN_str: str=  None, verbose=True)-> pd:
    """
    Convert the columns from timestamp to str with the default format.
    For ns details use:  format = "%Y-%m-%d %H:%M:%S.%f"

    Note:
    Args: if columns are empty every timestamp column will be transformed
    """
    # if we have no columns we use the whole dataframe
    if not columns:
        print("Using all columns")
        columns = list(data_pd.columns)
    if verbose:
        print(columns)
    for col in columns:
        if pd.core.dtypes.common.is_datetime_or_timedelta_dtype(data_pd[col]):
            if verbose:
                print(f"Convert column {col} to string")
            data_pd[col]= data_pd[col].dt.strftime(format)
            if replace_NaN_str is not None:
                data_pd[col] = data_pd.apply(lambda x: replace_NaN_str if pd.isnull(x[col]) else x[col], axis=1)  
    return data_pd
