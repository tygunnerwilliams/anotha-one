import requests
import openai
from config_final import Config
from utils import fetch_google_search_results, extract_stock_price_from_google, extract_news_headlines_from_google


class DataManager:

    def __init__(self):
        self.api_key = Config.GOOGLE_SEARCH_API_KEY

    def get_stock_price(self, stock_name):
        query = f'{stock_name} stock price'
        results = fetch_google_search_results(query)
        return extract_stock_price_from_google(results)

    def get_stock_news(self, stock_name):
        query = f'{stock_name} news'
        results = fetch_google_search_results(query)
        return extract_news_headlines_from_google(results)

    def get_sentiment(self, text):
        openai.api_key = Config.OPENAI_API_KEY
        response = openai.Completion.create(engine='gpt-4', prompt=f'What is the sentiment of this text: "{text}"? Positive, Negative, or Neutral?', max_tokens=50)
        sentiment = response.choices[0].text.strip()
        return sentiment