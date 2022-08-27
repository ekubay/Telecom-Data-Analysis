#System Modules
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
#sys.path.insert(0, './pages')
sys.path.insert(0, './tests')
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
import dashboard.user_satisfuction_analysis as satisfy

#st.title("Telecomunication Data analysis2")
#st.sidebar.markdown("# Tellcomunication Data Analysis")
#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
with st.sidebar:
<<<<<<< HEAD
=======
  #'Engagement', 'Experience', 'Satisfaction'
   #'bi-cloud-check-fill', 'bi-briefcase-fill','bi-check-square-fill'], menu_icon="cast", 
>>>>>>> 4ebdc20d68cf3cc3376168af8779128e5214371e
  page = option_menu('Menu', ['Main', 'Overview','Engagement', 'Experience', 'Satisfaction'],
                            icons=['house', 'bi-currency-exchange','bi-cloud-check-fill', 'bi-briefcase-fill',
                            'bi-check-square-fill'], menu_icon="cast", default_index=1)
  page
  
  
  df = pd.read_csv('clean_df_tel1.csv')
  #df1 = pd.read_csv('tele-data.csv')

  overview = OverviewAnalysis(df)
  #engagement = engagementAnalysis(df)
  #expriance = exprianceAnalysis(df1)
  #satisfaction = satisfactionAnalysis(df)
  #df = pd.read_csv('data/clean_df_tel1.csv')
  if(page == 'Main'):
   main1.run()
  elif(page == 'Overview'):
   overview.run_overview()
  elif(page == 'Engagement'):
    engage.run_engagement()
  elif(page == 'Experience'):
    expriance.run_experiance()
  elif(page == 'Satisfaction'):
    satisfy.run_satisfaction()
  else:
    main1.run()