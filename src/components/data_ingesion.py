import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import *
from src.exception import CustomException
from src.logger import logging
import os
import sys
from src.utils import *

@dataclass
class DataIngesionConfig:
    collection, db, client = mongo_connect()
    data = r'artifacts/data.csv'
    full_data = r'artifacts/full_data.csv'
    notebook_data = r'notebook/data.csv'
    notebook_full_data = r'notebook/full_data.csv'


class DataIngesion:
    def __init__(self) -> None:
        self.config = DataIngesionConfig
        os.makedirs(os.path.dirname(self.config.data), exist_ok=True)
        pd.read_csv(self.config.notebook_data).to_csv(self.config.data)
        pd.read_csv(self.config.notebook_full_data).to_csv(self.config.full_data)

    def get_data(self, location='local') -> pd.DataFrame:
        if location == 'local':
            return pd.read_csv(self.config.data)
        
        elif location == 'local_full':
            return pd.read_csv(self.config.full_data)
        
        elif location == 'database':
            try:
                all_data, actual_data = mongo_to_df(self.config.collection)
                logging.info('Got data from Database successfully')
                return all_data, actual_data
            except Exception as e:
                raise CustomException(e, sys)
    
    

