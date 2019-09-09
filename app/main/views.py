from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_Sources(), get_everything, get_top_headlines
from ..models import Sources, Top_Headlines, Everything 

# views
@main.route('/')
def index():
    '''
    view root function that returns the index page and its data
    '''
    Sources = get_Sources
    Everything = get_everything
    print(Sources)

    title = 'News Top highlights'
    return render_template(title= title,Sources=Sources,Everything=Everything)

@main.route('sources/<sources>')
def Top_Headlines(Sources):
    sources = get_Sources()
    Top_Headlines = get_top_headlines(source)
    print(Top_Headlines)

    return render_template('Top-headlines.html',sources=sources,Top_Headlines=Top_Headlines)
    