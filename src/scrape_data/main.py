"""
@name: main.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 30, 2018
"""
import datetime
from scrape_data.services.scrape_service import ScrapeService


if __name__ == '__main__':
    page = 'bbcnews'
    path = '../data/'

    sc = ScrapeService(page, path)

    start_time = datetime.datetime.now()
    print("Start: {}".format(start_time))

    #sc.start()

    end_time = datetime.datetime.now()
    print "Done\n Time: {}".format(end_time - start_time)
