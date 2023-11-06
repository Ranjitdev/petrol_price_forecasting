import streamlit as st
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import *
from src.exception import CustomException
from src.logger import logging
import os
import sys
from src.utils import *
from src.components.data_ingesion import DataIngesion


class DatabaseQueryFilters:
    def __init__(self) -> None:
        self.local_data = DataIngesion().get_data('local')
        self.local_full_data = DataIngesion().get_data('local_full')
        self.database_all_data, self.database_actual_data = DataIngesion().get_data('database')
        self.collection, self.db, self.client = mongo_connect()


    def year_day_month_filter(self, my_year, my_month, my_day):
        try:
            # Pinging mongodb for connection test
            self.client.admin.command('ping')
            logging.info('Ping done successfully to MongoDB')
            my_collection = self.collection

            found = []
            if my_year == 'Select' and my_month == 'Select' and my_day == 'Select':
                for i in my_collection.find():
                    found.append(i)

            elif my_year != 'Select' and my_month != 'Select' and my_day == 'Select':
                for i in my_collection.find({'Year': my_year, 'Month': my_month}):
                    found.append(i)
            elif my_year != 'Select' and my_month == 'Select' and my_day != 'Select':
                for i in my_collection.find({'Year': my_year, 'Day': my_day}):
                    found.append(i)
            elif my_year == 'Select' and my_month != 'Select' and my_day != 'Select':
                for i in my_collection.find({'Day': my_day, 'Month': my_month}):
                    found.append(i)

            elif my_year != 'Select' and my_month == 'Select' and my_day == 'Select':
                for i in my_collection.find({'Year': my_year}):
                    found.append(i)
            elif my_year == 'Select' and my_month != 'Select' and my_day == 'Select':
                for i in my_collection.find({'Month': my_month}):
                    found.append(i)
            elif my_year == 'Select' and my_month == 'Select' and my_day != 'Select':
                for i in my_collection.find({'Day': my_day}):
                    found.append(i)

            return pd.DataFrame(found)
        except Exception as e:
            raise CustomException(e, sys)


class DatabaseQuery(DatabaseQueryFilters):
    def __init__(self) -> None:
        super().__init__()
        pass

    def view_actual_data(self):
        col1, col2, col3 = st.columns(3)
        st.caption('Hover and click extend to view full screen')
        pivot_table = make_pivot(self.database_all_data)

        with col1:
            st.title('Petrol price (USD)')
            st.dataframe(self.database_actual_data)
            # Download option
            actual_data_df = self.database_actual_data.to_csv()
            st.download_button(label='Download', data=actual_data_df, file_name='Data.csv', mime='text/csv')
        with col2:
            st.title('Description')
            st.dataframe(self.database_actual_data.describe())
        with col3:
            st.title('Pivot Table')
            st.dataframe(pivot_table)
            # Download option
            pivot_table_df = pivot_table.to_csv()
            st.download_button(label='Download', data=pivot_table_df, file_name='Summary.csv', mime='text/csv')

    def petrol_price(self):
        full_data = DataIngesion().get_data('local_full')
        years = full_data['Year'].unique()
        months = full_data['Month'].unique()
        days = full_data['Day'].unique()

        # Select boxes for year month day
        col1, col2, col3 = st.columns(3)
        st.caption('Hover and click extend to view full screen')

        with col1:
            Year = st.selectbox('Year', ['Select'] + list(years))
        with col2:
            Month = st.selectbox('Month', ['Select'] + list(months))
        with col3:
            Day = st.selectbox('Day', ['Select'] + list(days))
        
        # Selected year month day to filter
        found = self.year_day_month_filter(str(Year), str(Month), str(Day))
        pivot_table = make_pivot(found)
        found = found.drop(['_id', 'Year', 'Month', 'Day'], axis=1)
        logging.info(f'Query done for {Year}, {Month}, {Day}')

        col4, col5, col6 = st.columns(3)
        with col4:
            st.header('Petrol Price (USD)')
            st.dataframe(found, hide_index=True)
            # Download option
            st.download_button(label='Download', data=found.to_csv(), file_name='Data.csv', mime='text/csv')
        with col5:
            st.header('Pivot Table')
            st.dataframe(pivot_table)
            # Download option
            st.download_button(label='Download', data=pivot_table.to_csv(), file_name='Pivot.csv', mime='text/csv')
        with col6:
            st.header('Description')
            st.dataframe(found.describe())
