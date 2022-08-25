#System Modules
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
#sys.path.insert(0, './pages')
#import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu 
# the pages
import pages.main as main1
from pages.user_overview_analysis import OverviewAnalysis
#from pages.user_engagement_analysis import engagementAnalysis
#from pages.user_expriance_analysis import exprianceAnalysis
#from pages.user_satisfuction_analysis import satisfactionAnalysis

# reading the file 
df = pd.read_csv('data/clean_df_tel1.csv')

st.set_page_config(page_title="Telecom Data Analysis", layout="wide")
st.title("Telcom Data analysis")
st.sidebar.markdown("# TellCo Data Analysis")
#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
with st.sidebar:
  #'Engagement', 'Experience', 'Satisfaction'
   #'bi-cloud-check-fill', 'bi-briefcase-fill','bi-check-square-fill'], menu_icon="cast", 
  page = option_menu('Menu', ['Main', 'Overview'],
                            icons=['house', 'bi-currency-exchange'],
                            
                           default_index=1)
  page
  
  overview = OverviewAnalysis(df)
  #engagement = engagementAnalysis(df)
  #expriance = exprianceAnalysis(df)
  #satisfaction = satisfactionAnalysis(df)


if(page == 'Main'):
  main1.run()
elif(page == 'Overview'):
  overview.run_overview()
# elif(page == 'Engagement'):
#   enngagement.run_engagement()
# elif(page == 'Experience'):
#   experience.run_experiance()
# elif(page == 'Satisfaction'):
#   satisfaction.run_satisfaction()
else:
  main1.run()
