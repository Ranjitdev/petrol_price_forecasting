# Project Title: Petrol Price Forecasting

**ONGCF is an oil and natural gas organization. It has data available for price at a weekly level. It wants to predict the price for crude oil for the next 16 months, starting from 1st Jan 2019 to April 2020.**
**MAPE is the evaluation metric that will be used in this case to evaluate output.**

## Data Description
- **The data contains petrol prices(Petrol (USD)) and Date column in train_data.csv. The test data has the dates for which the predictions are to be made(column names Date and Prediction), corresponding to which Prediction is blank. You are supposed to make the prediction and submit the file in that form.**
- Link: [Here](https://www.kaggle.com/c/petrol-price-forecasting/data)
- Train Data: [Here](notebook/train_data.csv)
- Test Data: [Here](notebook/test_data.csv)
- Sample Submission Data: [Here](notebook/sample_submission.csv)
- Evaluation Matrix: [Here](https://www.statisticshowto.com/mean-absolute-percentage-error-mape#:~:text=The%20mean%20absolute%20percentage%20error,values%20divided%20by%20actual%20values.e)

## Setup
- Create virtual enviroment:
  - > conda create -p venv python=3.9 -y
- Activate the virtual enviroment
  - > conda activate venv/
- Install required packages
  - > pip install -r requirements.txt
- Install setup
  - > python setup.py install
