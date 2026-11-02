import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

class Config:

    INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
    INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
    TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')
    TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
    TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')


    # Flask secret key


    # Paths
    DATA_DIR = 'data'
    REPORTS_DIR = 'reports'
    REFERENCE_DATA = 'data/reference_data.csv'
    
    # Proxy settings
    PROXY_FILE = 'valid_proxies.txt'

    @classmethod
    def verify(cls):
        missing = []
        if not cls.INSTAGRAM_USERNAME: missing.append('INSTAGRAM_USERNAME')
        if not cls.INSTAGRAM_PASSWORD: missing.append('INSTAGRAM_PASSWORD')
        if not cls.TWITTER_BEARER_TOKEN: missing.append('TWITTER_BEARER_TOKEN')
        if not cls.TELEGRAM_API_ID: missing.append('TELEGRAM_API_ID')
        if not cls.TELEGRAM_API_HASH: missing.append('TELEGRAM_API_HASH')
        
        if missing:
            raise ValueError(f"Missing configuration: {', '.join(missing)}")