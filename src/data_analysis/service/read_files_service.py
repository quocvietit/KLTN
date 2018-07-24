"""
@name: read_files_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import logging
import os
import codecs
from data_analysis import setting

class ReadFilesService:
	def __init__(self):
		self.__path = setting.DATA_TRAIN_PATH

	def start(self):
		logging.info("Read files")
		file_paths = self.get_paths()

		doc_complete = []
		for file_path in file_paths:
			fp = codecs.open(file_path, 'r', 'utf-8')
			doc_content = fp.read()
			doc_complete.append(doc_content)

		#print(doc_complete)
		print(len(doc_complete))

	def get_paths(self):
		file_paths = [os.path.join(self.__path, p) for p in os.listdir(self.__path)]
		return file_paths
