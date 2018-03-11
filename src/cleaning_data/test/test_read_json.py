"""
@name: read_json
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 28, 2018
"""
import json

from cleaning_data.service.get_data_service import GetDataService

path = '../../data/bbcnews_posts_2012.json'
with open(path, 'r') as f:
    while True:
        data = f.readline()
        data = json.loads(data)
        print data
        data = GetDataService(data)
        print data.get_created_time(), data.get_status_type()
