from isort import file
import streamlit as st
from src.components.data_ingesion import DataIngesion
from src.utils import *

with st.sidebar:
    option = st.radio(
        ['Forecast', 'Old Prices', 'Graphs'],
        captions=[
            'Forecasting price & Enter new data', 'View excel file', 'Graphs and Charts'
        ]
    )

if option == 'Forecast':
    pass

elif option == 'Old Prices':
    all_data, actual_data = DataIngesion().get_data('database')
    pivot_table = make_pivot(all_data)

    col1, col2 = st.columns(2)
    st.caption('Hover and click extend to view full screen')

    with col1:
        st.title('Petrol price (USD)')
        st.dataframe(actual_data)

        actual_data_df = actual_data.to_csv()
        st.download_button(label='Download', data=actual_data_df, file_name='Data.csv', mime='text/csv')
    with col2:
        st.title('Summary price (USD)')
        st.dataframe(pivot_table)

        pivot_table_df = pivot_table.to_csv()
        st.download_button(label='Download', data=pivot_table_df, file_name='Data.csv', mime='text/csv')

elif option == 'Graphs':
    pass
