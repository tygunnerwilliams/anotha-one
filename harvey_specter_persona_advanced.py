import requests
import openai
import random
from config_final import Config
from data_manager import DataManager


class HarveySpecterPersona:

    def __init__(self):
        self.data_manager = DataManager()

    def get_stock_info(self, stock_name):
        return self.data_manager.get_stock_price(stock_name)

    def get_stock_news(self, stock_name):
        return self.data_manager.get_stock_news(stock_name)

    def give_advice(self, stock_name):
        # Fetch data
        stock_price = self.get_stock_info(stock_name)
        news_headlines = self.get_stock_news(stock_name)
        
        # Set the context for Harvey Specter's personality
        harvey_contexts = [
            "You are Harvey Specter, a top lawyer with a sharp wit and confidence.",
            "Imagine you're Harvey Specter, standing tall in your office overlooking Manhattan, and someone asks for your advice on stocks.",
            "You are Harvey Specter, the best closer in New York City. With a glass of scotch in hand, you're about to give a piece of advice on stocks.",
            "Channeling the confidence and charisma of Harvey Specter, what would you say about this stock?"
        ]
        
        harvey_context = random.choice(harvey_contexts)
        
        # Combine the context, data, and the actual question
        full_question = f"{harvey_context} The current stock price of {stock_name} is {stock_price}. Here are some recent news headlines related to it: {news_headlines}. What's your take on this?"
        
        # Query ChatGPT
        response = openai.Completion.create(engine='gpt-4', prompt=full_question, max_tokens=150)
        
        return response.choices[0].text.strip()