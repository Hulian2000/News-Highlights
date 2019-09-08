import os

class Config:
    NEWS_HIGHLIGHT_BASE_URL ='https://newsapi.org/v2/sources?&apiKey={}'
    API_KEY = os.environ.get('API_KEY')
    TOP_HEADLINES_URL ='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    EVERYTHING_URL_KEY ='https://newsapi.org/v2/everything?domains=wsj.com,nytimes.com&apiKey={}'

class ProdConfig(Config):
    '''
    Production configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    '''
    DEBUG = True
    ENV = 'development'

config_options = {
    'development'= DevConfig,
    'production' = ProdConfig
}