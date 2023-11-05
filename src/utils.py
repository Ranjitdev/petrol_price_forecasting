import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dataclasses import dataclass
from typing import List, Tuple
from src.exception import CustomException
from src.logger import logging
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import sys


def mongo_to_df(collection) -> pd.DataFrame:
    lis = []
    all_data = None
    try:
        for i in collection.find():
            lis.append(i)
        all_data = pd.DataFrame(lis)
        actual_data = all_data.set_index('Date').drop(['_id', 'Year', 'Month', 'Day'], axis=1)
        logging.info(f'Found {collection} in database converted into dataframe successfully')
        return all_data, actual_data
    except Exception as e:
        raise CustomException(e, sys)

def make_pivot(df) -> pd.DataFrame:
    return pd.pivot_table(
        df, values='Price', index='Month', columns='Year', aggfunc='sum', margins=True, margins_name='Total'
        )

def mongo_connect():
    try:
        mongo_url = "mongodb+srv://root:12345678rk@rkdatabase.yig0aad.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(mongo_url, server_api=ServerApi('1'))
        client.admin.command('ping')
        db = client['project_forecasting']
        my_collection = db['petrol_price_usd']
        logging.info('Connected to the Database')
        return my_collection, db, client
    except Exception as e:
        raise CustomException(e, sys)


