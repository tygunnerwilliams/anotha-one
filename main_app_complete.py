import sys
import requests
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QTextEdit, QSlider, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont, QPalette
from harvey_specter_persona_advanced import HarveySpecterPersona
from models import StockPredictor
from config_final import Config
from utils import fetch_google_search_results, extract_stock_price_from_google, extract_news_headlines_from_google
from data_manager import DataManager

class HarveySpecterApp(QMainWindow):
    def __init__(self, persona):
        super().__init__()
        self.persona = persona
        self.stock_predictor = StockPredictor('random_forest')
        self.init_ui()

def init_ui(self):
        self.setWindowTitle('Harvey Specter AI Trader')
        self.setGeometry(100, 100, 800, 600)
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Highlight, QColor(142, 45, 197).lighter())
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)
        font = QFont()
        font.setBold(True)
        font.setPointSize(14)
        self.title_label = QLabel(self)
        self.title_label.setText('Harvey Specter AI Trader')
        self.title_label.setFont(font)
        self.title_label.move(250, 10)
        self.stock_input = QLineEdit(self)
        self.stock_input.move(100, 50)
        self.fetch_button = QPushButton('Fetch Stock Price', self)
        self.fetch_button.move(100, 80)
        self.fetch_button.clicked.connect(self.fetch_stock_price)
        self.stock_price_display = QLabel('Stock Price will be displayed here', self)
        self.stock_price_display.move(100, 110)

def fetch_stock_price(self):
        stock_name = self.stock_input.text()
        price = DataManager.get_stock_price(stock_name)
        self.stock_price_display.setText(f'Stock Price for {stock_name}: {price}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    persona = HarveySpecterPersona()
    mainWin = HarveySpecterApp(persona)
    mainWin.show()
    sys.exit(app.exec_())