import numpy as np
import pandas as pd
import openai
import os
from sklearn.ensemble import RandomForestRegressor
from statsmodels.tsa.arima.model import ARIMA
from sklearn.svm import SVR
from config_final import Config
from utils import fetch_google_search_results

class StockPredictor:

    def __init__(self, stock_name):
        self.stock_name = stock_name
        self.data_dir = 'data'
        self.data_file = f'{self.data_dir}/{stock_name}_historical_data.txt'
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        if os.path.exists(self.data_file):
            self.historical_data = self.load_data_from_file()
        else:
            self.historical_data = self.fetch_historical_data()
            self.save_data_to_file()

    def fetch_historical_data(self):
        prompt = f"Provide the historical stock prices for {self.stock_name} for the past 100 days."
        response = openai.Completion.create(engine='gpt-4', prompt=prompt, max_tokens=150, api_key=Config.CHATGPT_API_KEY)
        data_str = response.choices[0].text.strip()
        data_list = [float(price) for price in data_str.split() if price.replace('.', '', 1).isdigit()]
        return data_list

    def save_data_to_file(self):
        with open(self.data_file, 'w') as f:
            for price in self.historical_data:
                f.write(f'{price}\n')

    def load_data_from_file(self):
        with open(self.data_file, 'r') as f:
            data = [float(line.strip()) for line in f.readlines()]
        return data

    def random_forest_predictor(self):
        train = self.historical_data[:-30]
        test = self.historical_data[-30:]
        x_train = np.array(range(len(train))).reshape(-1, 1)
        y_train = train
        x_test = np.array(range(len(train), len(train) + len(test))).reshape(-1, 1)
        model = RandomForestRegressor(n_estimators=100)
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        return predictions

    def arima_predictor(self):
        model = ARIMA(self.historical_data, order=(5,1,0))
        model_fit = model.fit(disp=0)
        predictions = model_fit.forecast(steps=30)[0]
        return predictions

    def svr_predictor(self):
        train = self.historical_data[:-30]
        test = self.historical_data[-30:]
        x_train = np.array(range(len(train))).reshape(-1, 1)
        y_train = train
        x_test = np.array(range(len(train), len(train) + len(test))).reshape(-1, 1)
        model = SVR(kernel='rbf', C=1e3, gamma=0.1)
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        return predictions