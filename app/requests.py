import urllib.request,json
from .models import Source, Article

# Getting api key
api_key = None

#source url as a variable
source_url = None

def configure_request(app):

    global api_key, source_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['NEWS_SOURCES_URL']
    print(source_url)
    print(api_key)

def get_source():
    get_source_url = source_url.format(api_key)
    print (get_source_url)

    with urllib.request.urlopen(get_source_url)as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None
        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

def process_results(source_list):
    source_results = []
    for source in source_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        language = source.get('language')

        if name:

            source_object =  Source(id,name,description,language)
            source_results.append(source_object)

    return source_results

def get_article(id):
    get_article_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['articles']
            article_results = process_articles(article_results_list)

    return article_results

      #processing the article json
def process_articles(article_list):
    article_results = []
    for article in article_list:
        author = article.get('author')
        title = article.get ('title')
        description = article.get('description')
        url = article.get('url')
        image = article.get('urlToImage')
        time = article.get('publishedAt')

        if title:
            article_object = Article(author,title,description,url,image,time)
            article_results.append(article_object)

    return article_results

def get_category(name):
    get_category_url = 'https://newsapi.org/v2/everything?q={}&sortBy=relevancy&apiKey={}'.format(name,api_key)
    with urllib.request.urlopen(get_category_url) as url:
        get_category_data = url.read()
        get_cartegory_response = json.loads(get_category_data)

        get_cartegory_results = None

        if get_cartegory_response['articles']:
            get_cartegory_list = get_cartegory_response['articles']
            get_cartegory_results = process_articles(get_cartegory_list)

    return get_cartegory_results