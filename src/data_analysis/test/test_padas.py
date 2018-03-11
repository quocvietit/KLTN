"""
@name: test_padas
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 10, 2018
"""
import pandas
import json
import matplotlib

f = open("../../data/bbcnews_posts_2012_v2.json", 'r')
js = json.load(f)
print(js)
fs = pandas.DataFrame(js)
col = ["reactions", "shares", "comments"]
fs['created_time'] = fs.created_time_day.map(str) + "/" + fs.created_time_month.map(
    str) + "/" + fs.created_time_year.map(str)
print fs.describe()
print fs.like.hist(bins = 50)
