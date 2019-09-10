from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_everything,get_top_headlines
from ..models import Sources

# views
@main.route('/')
def index():
    '''
    view root function that returns the index page and its data
    '''
    sources = get_sources()
    Everything = get_everything()
    print(sources)

    title = 'News Top highlights'
    return render_template('index.html',title= title,sources=sources,Everything=Everything)

@main.route('/sources/<sources>')
def Top_Headlines(sources):
    sources = get_sources()
    Top_Headlines = get_top_headlines(source)
    print(Top_Headlines)

    return render_template('Top-headlines.html',sources=sources,Top_Headlines=Top_Headlines)
    