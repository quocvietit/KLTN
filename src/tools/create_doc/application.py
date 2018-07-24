"""
@name: application
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 22, 2018
"""

import sys

reload(sys)
sys.setdefaultencoding('utf8')

import datetime
from tools.create_doc.handler_file import HandlerFile as HF

if __name__ == '__main__':
	hf = HF('../../data/bbcnews/post_data_07042018', '../../data')

	start_time = datetime.datetime.now()
	print "-------------------------------"
	print("Start: {}".format(start_time))

	res = hf.start()

	end_time = datetime.datetime.now()
	print "Done\n Time: {} ".format(end_time - start_time)
	print "Res: {} doc".format(res)
	print "-------------------------------"


