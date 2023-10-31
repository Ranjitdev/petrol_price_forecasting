from setuptools import setup, find_packages
from typing import List

Project = 'Petrol Price Forecasting'
Version = 1.0
Author = 'Ranjit Kundu'
Description = r'https://www.kaggle.com/c/petrol-price-forecasting/data'


def get_requirements() -> List[str]:
    with open('requirements.txt', 'r') as file:
        required_list = file.readlines()
        required_list = [i.replace('\n', '') for i in required_list]
        required_list.remove('-e .')
        return required_list


setup(
    name=Project,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(),
    install_requires=get_requirements()
)