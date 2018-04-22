"""
@name: setting
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATA_TRAIN_PATH = os.path.join(DIR_PATH, 'data/data_2012/train/')
DATA_TEST_PATH = os.path.join(DIR_PATH, 'data/10_cate/test/')
DATA_TRAIN_JSON = os.path.join(DIR_PATH, 'data_train.json')
DATA_TEST_JSON = os.path.join(DIR_PATH, 'data_test.json')
DATA = os.path.join(DIR_PATH, 'data')
LANGUAGE = "english"
LOGGING = os.path.join(DIR_PATH, 'log')
FORMAT_LOGGING = "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] - %(message)s"
FORMAT_DATE = '%m/%d/%Y %I:%M:%S %p'