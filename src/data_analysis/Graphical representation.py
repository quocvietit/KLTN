"""
@name: Graphical representation
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 26, 2018
"""
import os
import json
import pandas as pd
import numpy as np
import matplotlib as plt

file_path = "../data"
file_name = "bbcnews_posts_2012_v3.json"

file_data = open( file_path + "/" + file_name, "r")

json_data = json.load(file_data)

df = pd.DataFrame(json_data)

col = ['id','reactions','shares','comments']
print df[col].head()



df['reactions_log'] = np.log(df.reactions)
print df.reactions_log.hist(bins = 50)