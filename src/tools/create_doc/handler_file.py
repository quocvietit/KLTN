"""
@name: handler_file
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import os
import codecs
import json


class HandlerFile:
	def __init__(self, file_path, dir_path):
		self.__path = file_path
		self.__dir = dir_path
		self.__count = 0

	def start(self):
		self.check_dir()
		try:
			file_paths = [os.path.join(self.__path, p) for p in os.listdir(self.__path)]
			doc_complete = []
			for file_path in file_paths:
				fp = codecs.open(file_path, 'r', 'utf-8')
				try:
					datas= json.loads(fp.read())
					for data in datas:
						file_name = data['id']
						path = os.path.join(self.__dir + "/" + "post_contents", file_name)
						content = data['message']
						if content not in "No message":
							with codecs.open(path, "w", 'utf-8') as f:
								f.write(content)
								f.close()
								self.__count+=1
				except Exception as ex:
					print "Error load: ", ex

		except IOError as ex:
			print("Error: " + str(ex))

		return self.__count

	def check_dir(self):
		if not os.path.exists(self.__dir + "/" + "post_contents"):
			os.makedirs(self.__dir + "/" + "post_contents")
