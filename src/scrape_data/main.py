"""
@name: main.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 30, 2018
"""
import datetime
from scrape_data.services.scrape_service import ScrapeService


def scrap(page, path, since, until):
    sc = ScrapeService(page, path, since, until)

    start_time = datetime.datetime.now()
    print "-------------------------------"
    print("Start: {}".format(start_time))

    sc.start()

    end_time = datetime.datetime.now()
    print "Done\n Time: {} ".format(end_time - start_time)
    print "-------------------------------"


if __name__ == '__main__':
    print "Scrape Data"
'''
    pages = ['VOATiengViet',
             'voiceofamerica']
    path = '../data/'

    for page in pages:
        print "Page info"
       ScrapeService(page, path, '', '').scrape_page_info()

        print "2017"
        scrap(page, path, '2017-01-01', '2017-12-31')
    
        print "2016"
        scrap(page, path, '2016-01-01', '2016-12-31')

        print "2015"
        scrap(page, path, '2015-01-01', '2015-12-31')

        print "2014"
        scrap(page, path, '2014-01-01', '2014-12-31')

        print "2013"
        scrap(page, path, '2013-01-01', '2013-12-31')

        print "2012"
        scrap(page, path, '2012-01-01', '2012-12-31')
'''
