#System Modules
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
#sys.path.insert(0, './pages')
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from insert_data  import db_execute_fetch
import script.ploting_fun as plot
#This is User Averview Analysis
#st.set_page_config(page_title="Day 5", layout="wide")

def loadData():
    query = "select * from TelecomDataTable"
    df = db_execute_fetch(query, dbName="Telecom_db", rdf=True)
    return df

st.set_option('deprecation.showPyplotGlobalUse', False)
def run_overview():
  df = loadData()
  st.write("User Overview Analysis")
    # reading the file 
    #file_name = 'clean_df_tel.csv'
    #file_name = 'clean_df_tel1.csv.csv'
    #df_overview = pd.read_csv(file_name)
  top_10_handset = df.groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(10)
  top_3_manufacturers = df.groupby("Handset Manufacturer")['MSISDN/Number'].nunique().nlargest(3)

  fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(12,7))
  plot.serious_bar(top_3_manufacturers, ax1)
  plot.serious_bar(top_10_handset, ax2)
  plt.xticks(rotation=75)
  st.pyplot()

  top_manufacturers = df.groupby("Handset Manufacturer").agg({"MSISDN/Number":'count'}).reset_index()
  top_3_manufacturers = top_manufacturers.sort_values(by='MSISDN/Number', ascending=False).head(3)
  manufacturers = df.groupby("Handset Manufacturer")
  st.write("The top 5 handsets per top 3 handset manufacturer")

    # Top five Handset Type in the top 3 manufacturing 

  for column in top_3_manufacturers['Handset Manufacturer']:
    result = manufacturers.get_group(column).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(5)
    st.write(f"**** { column } ***")
    print("i am at the overview")
    print(result)
    st.write(result.head())
    st.write(" Overview Analysis outcomes")
    st.write("overall analysis")
