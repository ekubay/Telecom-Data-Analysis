#System Modules
import os
import sys
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.insert(0, './pages')
#import numpy as np
#import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu 
# the pages
import pages.main as main1
import pages.user_overview_analysis as overview
import pages.user_engagement_analysis as enngagement
import pages.user_expriance_analysis as experience
import pages.user_satisfuction_analysis as satisfaction

st.set_page_config(page_title="Telecom Data Analysis", layout="wide")
st.title("TelCo Data analysis")
st.sidebar.markdown("# TellCo Data Analysis")
#page = st.sidebar.selectbox('TellCo Menu', ['Intro', 'Marketing', 'Engagement', 'Experiance', 'Satisfaction'])
with st.sidebar:
  page = option_menu('TellCo Menu', ['Main', 'overview analysis', 'Engagement', 'Experience', 'Satisfaction'],
                            icons=['house', 'bi-currency-exchange','bi-cloud-check-fill', 'bi-briefcase-fill','bi-check-square-fill'], menu_icon="cast", default_index=1)
  page
if(page == 'Home'):
  main1.run()
elif(page == 'Overview')
  marketing.run_verview()
elif(page == 'Engagement'):
  enngagement.run_engagement()
elif(page == 'Experience'):
  experience.run_experiance()
elif(page == 'Satisfaction'):
  satisfaction.run_satisfaction()
else:
  main1.run()
