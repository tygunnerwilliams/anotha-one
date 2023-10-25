import requests
from config_final import Config
from textblob import TextBlob
from models import StockPredictor


def fetch_google_search_results(query):
    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": Config.GOOGLE_SEARCH_API_KEY,
        "cx": Config.GOOGLE_SEARCH_ENGINE_ID,
        "q": query
    }
    response = requests.get(endpoint, params=params)
    return response.json()


def extract_stock_price_from_google(query):
    results = fetch_google_search_results(query)
    for item in results.get('items', []):
        if "stock price" in item.get('title', '').lower():
            return item.get('title', '').split()[-1]
    return None


def extract_news_headlines_from_google(query):
    results = fetch_google_search_results(query + " news")
    headlines = []
    for item in results.get('items', []):
        headlines.append(item.get('title', ''))
    return headlines


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def get_historical_prices(stock_name):
    # Use the StockPredictor class from models.py to fetch historical prices
    predictor = StockPredictor(stock_name)
    historical_prices = predictor.get_historical_data()
    return historical_prices