import pandas as pd
import numpy as np
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging
import os
import sys
from src.utils import *

@dataclass
class DataIngesionConfig:
    mongo_url = "mongodb+srv://root:12345678rk@rkdatabase.yig0aad.mongodb.net/?retryWrites=true&w=majority"
    client = MongoClient(mongo_url, server_api=ServerApi('1'))
    data = r'artifacts/data.csv'
    notebook_data = r'notebook/data.csv'


class DataIngesion:
    def __init__(self) -> None:
        self.config = DataIngesionConfig
        os.makedirs(os.path.dirname(self.config.data), exist_ok=True)
        pd.read_csv(self.config.notebook_data).to_csv(self.config.data)

    def get_data(self, location='local') -> pd.DataFrame:
        if location == 'local':
            return pd.read_csv(self.config.data)
        
        elif location == 'database':
            try:
                client = self.config.client
                client.admin.command('ping')

                db = client['project_forecasting']
                my_collection = db['petrol_price_usd']

                all_data, actual_data = mongo_to_df(my_collection)
                logging.info('Got data from Database successfully')

                return all_data, actual_data
            except Exception as e:
                raise CustomException(e, sys)

