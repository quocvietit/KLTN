"""
@name: test_stopwords
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 18, 2018
"""

import pandas
import json
from nltk.stem.wordnet import WordNetLemmatizer

f = open("../../data/bbcnews_posts_2012_07042018.json", 'r')
js = json.load(f)
fs = pandas.DataFrame(js)
stopwords = dict()
for message in fs.message:
    for word in message.split(" "):
        stopwords[word] = stopwords.get(word, 0) + 1

print len(stopwords)
print stopwords


lemma = WordNetLemmatizer()

