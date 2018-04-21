"""
@name: install_library
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
import nltk


class InstallLibrary:
    def __init__(self):
        logging.info("Started install library")

        libraries = ['punkt', 'averaged_perceptron_tagger']

        for library in libraries:
            result = nltk.download(library)
            logging.debug("Install {}: {}".format(library, str(result).upper()))

        logging.info("Finished install library")