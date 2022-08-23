import pandas as pd
import numpy as np

def percent_of_null(df):
    nrows, ncols= df.shape
    size_df = nrows * ncols
    null_size = (df.isnull().sum()).sum()
    percent = round((null_size / size_df) * 100, 2)
    return f"The telecom dataset contains {percent}% missing values"
    
def drop_insignificant_columns(df):
    size_df = df.shape[0]
    col_list = df.columns
    insgnifican_col = []
    for column in col_list:
        col_value_null = df[column].isnull().sum()
        percent = round( (col_value_null / size_df) * 100 , 2)
        if(percent > 50):
            #print("hello")
            insgnifican_col.append(column)
        insgnifican_col.append('Dur. (ms).1') # some repittion with ms

    df = df.drop(insgnifican_col, axis=1)
    return df
def fix_outlier(df, column):
    df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].median(),df[column])
    
    return df[column]