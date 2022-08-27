#System Modules
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
#import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu 
st.set_page_config(page_title='Telecommunication Data Analysis1', page_icon=None, layout="centered", 
initial_sidebar_state="auto", menu_items=None)
# the pages
import dashboard.main as main1
from dashboard.user_overview_analysis import OverviewAnalysis
import dashboard.user_engagement_analysis as engage
import dashboard.user_expriance_analysis as expriance
from dashboard.user_satisfuction_analysis import SatisfuctionAnalysis


#with st.sidebar:
  #'Engagement', 'Experience', 'Satisfaction'
    #'bi-cloud-check-fill', 'bi-briefcase-fill','bi-check-square-fill'], menu_icon="cast", 
page = option_menu('Menu', ['Main', 'User_Overview','User_Engagement', 'User_Experience', 'User_Satisfaction'],
                              icons=['house', 'bi-currency-exchange','bi-cloud-check-fill', 'bi-briefcase-fill',
                              'bi-check-square-fill'], menu_icon="cast", default_index=1)
page
    
    
df = pd.read_csv('clean_df_tel1.csv')
    #file_name = 'data/tel-data.csv'

    #df1 = pd.read_csv(file_name)

overview = OverviewAnalysis(df)
    #engagement = engagementAnalysis(df)
    #expriance = exprianceAnalysis(df1)
satisfy = SatisfuctionAnalysis(df)
    #df = pd.read_csv('data/clean_df_tel1.csv')
if(page == 'Main'):
  main1.run()
elif(page == 'User_Overview'):
  overview.overview_analysis()
elif(page == 'User_Engagement'):
  engage.engagement_analysis()
elif(page == 'User_Experience'):
  expriance.experiance_analysis()
elif(page == 'User_Satisfaction'):
  satisfy.satisfaction_analysis()
else:
 main1.run()
