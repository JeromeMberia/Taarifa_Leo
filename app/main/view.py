from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_article,get_category
from ..models import Article
from ..models import Source

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    source = get_source()
    title = 'News Live'
    return render_template('index.html', title = title, source = source)

 
@main.route('/article/<article_id>')
def article(article_id):

    article = get_article(article_id)
    title = f'{article_id}'

    return render_template('article.html',id = article_id,title = title,article = article)

@main.route('/category/<cat_name>')
def category(cat_name):
  
    category = get_category(cat_name)
    print (category)
    title = f'{cat_name}'
    return render_template('category.html',title = title, category = category)