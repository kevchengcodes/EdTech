import pandas as pd
import numpy as np
import nltk
from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
from multiprocessing.dummy import Pool as ThreadPool
import psycopg2
from datetime import date, timedelta

import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

def getTxt(url):
    D={}
    article = Article(url)
    article.download()
    try:
        article.parse()
        article.nlp()
        #txt=article.title
        
        #dict['Media']=df['media'][ind]
        D['Title']=article.title
        D['Article']=article.text
        D['Summary']=article.summary
        D['Image'] = article.top_image
        D['Link'] = url
        D['Date']=article.publish_date
        return D
    except:
        return ""

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def save_topics(model, feature_names, no_top_words):
    alltopics = []
    for topic_idx, topic in enumerate(model.components_):
        alltopics.append(" ".join([feature_names[i]
                          for i in topic.argsort()[:-no_top_words - 1:-1]]))
    return alltopics

def NLP_news():
    # get the data
    #df = pd.read_json("Environment.json", lines=True)
    conn = psycopg2.connect("dbname=EdTech user=postgres password=edtech123")
    curr = conn.cursor()

    select = 'SELECT * FROM public.scrapenews_articlesclicked ORDER BY "Date" DESC;'
    curr.execute(select)
    rows = curr.fetchall()

    curr.close()
    conn.close()

    column_names = {"id", "Title", "Summary", "Article", "Image", "Link", "Date"}
    df = pd.DataFrame(rows, columns=column_names)

    # massage the data
    df['tokenized'] = df['Summary'].apply(word_tokenize)
    df['lower'] = df['tokenized'].apply(lambda x: [word.lower() for word in x])
    exclude = ['``','"',"''","'"]
    df['noquotes'] = df['lower'].apply(lambda x: [word for word in x if not any(e in word for e in exclude)])
    punc = string.punctuation
    df['no_punc'] = df['noquotes'].apply(lambda x: [word for word in x if word not in punc])
    stop_words = set(stopwords.words('english'))
    df['stopwords_removed'] = df['no_punc'].apply(lambda x: [word for word in x if word not in stop_words])
    df['pos_tags'] = df['stopwords_removed'].apply(nltk.tag.pos_tag)
    df['wordnet_pos'] = df['pos_tags'].apply(lambda x: [(word, get_wordnet_pos(pos_tag)) for (word, pos_tag) in x])
    wnl = WordNetLemmatizer()
    df['lemmatized'] = df['wordnet_pos'].apply(lambda x: [wnl.lemmatize(word, tag) for word, tag in x])
    df['lemma_str'] = [' '.join(map(str,l)) for l in df['lemmatized']]

    # NLP
    tfidf_vectorizer = TfidfVectorizer(max_df=0.90, min_df =25, max_features=5000, use_idf=True)
    tfidf = tfidf_vectorizer.fit_transform(df['lemma_str'])
    tfidf_feature_names = tfidf_vectorizer.get_feature_names()
    nmf = NMF(n_components=10, random_state=0, alpha=.1, init='nndsvd').fit(tfidf)

    # save topics
    no_top_words = 10
    topiclist = save_topics(nmf, tfidf_feature_names, no_top_words)

    return topiclist

def scrape_the_news():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent

    startdate = (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")
    enddate = date.today().strftime("%m/%d/%Y")
    googlenews=GoogleNews(start=startdate,end=enddate)

    topiclist = NLP_news()
    print(topiclist[0])
    googlenews.search(topiclist[1])
    result=googlenews.result()
    df=pd.DataFrame(result)
    urls = df['link'].tolist()

    # Initialize threads
    pool = ThreadPool(10)

    # open the urls in their own threads
    # and return the results
    results = pool.map(getTxt, urls)
    #results.tolist()

    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join()

    for i in range (0,len(results)):
        if results[i]:
            if not results[i]['Date']:
                results[i]['Date'] = df['datetime'][i].to_pydatetime()
            results[i]['Date'] = results[i]['Date'].strftime("%Y-%m-%d %H:%M:%S")


    conn = psycopg2.connect("dbname=EdTech user=postgres password=edtech123")
    curr = conn.cursor()
    #query = 'INSERT INTO public.scraper ("Title", "Summary", "Article", "Image", "Link", "Date") VALUES (%s %s %s %s %s)'

    for row in results:
        if row:
            columns = row.keys()
            values = [row[column] for column in columns]

            insert_statement = "INSERT INTO scrapenews_newslist VALUES (nextval('scrapenews_newslist_id_seq'::regclass),%s, %s, %s, %s, %s, %s)"
            curr.execute(insert_statement, tuple(values))

    conn.commit()

    curr.close()
    conn.close()