from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
import pandas as pd
import nltk
from multiprocessing.dummy import Pool as ThreadPool
import psycopg2
from datetime import date, timedelta

#config will allow us to access the specified url for which we are #not authorized. Sometimes we may get 403 client error while parsing #the link to download the article.
#nltk.download('punkt')

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

def scrape_the_news():
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent

    startdate = (date.today() - timedelta(days=1)).strftime("%m/%d/%Y")
    enddate = date.today().strftime("%m/%d/%Y")
    googlenews=GoogleNews(start=startdate,end=enddate)
    googlenews.search('Solar wind')
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
    query = 'INSERT INTO public.scraper ("Title", "Summary", "Article", "Image", "Link", "Date") VALUES (%s %s %s %s %s)'

    for row in results:
        if row:
            columns = row.keys()
            values = [row[column] for column in columns]

            insert_statement = "INSERT INTO scrapenews_newslist VALUES (nextval('scrapenews_newslist_id_seq'::regclass),%s, %s, %s, %s, %s, %s)"
            curr.execute(insert_statement, tuple(values))

    conn.commit()