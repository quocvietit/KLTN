"""
@name: logging
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
import os.path
from data_analysis.utils.version import get_version
from data_analysis import setting

def initialize_logger():
    version = get_version()
    file_log = "{}\logs_{}.txt".format(setting.LOGGING, version)

    if not os.path.exists(setting.LOGGING):
        os.makedirs(setting.LOGGING)

    if not os.path.isfile(file_log):
        with open(file_log, "w+") as f:
            f.write(version + "\n")
            f.close()

    level = logging.DEBUG
    format = setting.FORMAT_LOGGING
    datefmt = setting.FORMAT_DATE

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter(format, datefmt)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = logging.FileHandler(file_log, "a")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)