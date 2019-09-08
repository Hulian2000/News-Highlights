import urllib.request,json
from .models import Source, Everything, Top_headlines
from config import DevConfig

#Getting the Api key
api_key = None

# getting the base url
base_url = None
everything_url = None
headlines_url = None

def configure_request(app):
    global api_key, base_url ,everything_url, headlines_url

