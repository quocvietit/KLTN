"""
@name: main
@author: Vuong Quoc Viet
@version: 1.0
@since: Apr 21, 2018
"""

import logging
import datetime
from data_analysis.utils.logger_initializer import initialize_logger
from data_analysis.utils.install_library import InstallLibrary
from data_analysis.service.clean_text_service import CleanTextService

if __name__ == '__main__':
	initialize_logger()

	started = datetime.datetime.now()
	logging.info("Started")

	InstallLibrary()

	text = "this is a texts, 123, !@#$%^&*(, numbers cc, b, c,a, hello?"
	print (CleanTextService().start(text))

	finished = datetime.datetime.now()
	time = finished - started
	logging.info("Finished")
	logging.info("Time: {}s".format(finished - started))
