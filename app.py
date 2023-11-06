import streamlit as st
from src.components.database_query import DatabaseQuery
from src.utils import *

# Sidebar
with st.sidebar:
    option = st.radio('Select option',
        ['Forecast', 'Petrol Price (USD)', 'Graphs', 'Developer'],
        captions=[
            'Forecasting price & New Entry', 'View excel file of prices',
            'Graphs and Statistics of data', 'Developer option'
        ]
    )

# Forecasting and new data entry feature
if option == 'Forecast':
    pass

# Data Viewer
elif option == 'Petrol Price (USD)':
    DatabaseQuery().petrol_price()

# Graph plotting and graphical statistics
elif option == 'Graphs':
    pass

# Logs, Files and others
elif option == 'Developer':
    pass
