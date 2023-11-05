import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os
import sys
from typing import List, Tuple


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

        