import requests
import json
'''

a = requests.get("https://graph.facebook.com/v2.11/228735667216_10155546222577217/comments?access_token=315052069012915|6dd181af6083727c76678803e502d7e0",{'fields':'id,message,link'})
print a.url
print a.json()
'''

from scrape_data.services.comment_service import CommentService

with open('../data/bbcnews_posts_2017_2017.json') as f:
    for a in f.readlines():
        print json.loads(a)['id']
        print