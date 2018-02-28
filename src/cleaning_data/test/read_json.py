"""
@name: read_json
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 28, 2018
"""
from cleaning_data.service.file_service import FileService
from cleaning_data.models.data_post import DataPost
import json

path = '../../data/bbcnews_posts_2012.json'
with open(path, 'r') as f:
    while True:
        data = f.readline()
        data = json.loads(data)
        data = DataPost(data)
        print data.get_created_time(), data.get_status_type()
