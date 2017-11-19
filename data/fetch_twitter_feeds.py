from twython import Twython
import sys, csv, json

APP_KEY = 'YOUR_APP_KEY'
APP_SECRET = 'YOUR_APP_SECRET'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

reload(sys)
sys.setdefaultencoding('utf8')


def fetch_tweets(year=None, month=None):
    since = year + '-' + month + '-' + '01'
    until = year + '-' + month + '-' + '31'
    search = twitter.search(q='python', lang="en", n=2000, since=since, until=until)
    tweets = search['statuses']
    return tweets


years = [2017, 2016, 2015, 2014, 2013, 2012, 2011]
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for year in years:
    for month in months:
        mydict = fetch_tweets(year, month)
        file_str = './sensex_tweets/' + str(year) + '-' + '{:02}'.format(month) + '.json'
        with open(file_str, 'w') as fout:
            json.dump(mydict, fout)
        fout.close()
