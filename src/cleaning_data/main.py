"""
@name: main
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
import datetime
from cleaning_data.service.cleaning_data_service import CleaningDataService


def clean(path, file_name, version):
    cleaningData = CleaningDataService(path, file_name, version)
    print (file_name)
    cleaningData.start()


if __name__ == '__main__':
    path = '../data/'
    fileNames = ['bbcnews_posts_2012.json',
                 'bbcnews_posts_2013.json',
                 'bbcnews_posts_2014.json',
                 'bbcnews_posts_2015.json',
                 'bbcnews_posts_2016.json',
                 'bbcnews_posts_2017.json',
                 ]
    version = 'v1'
    start_time = datetime.datetime.now()
    print("Start: {}".format(start_time))

    for file in fileNames:
        clean(path, file, version)

    end_time = datetime.datetime.now()
    print "Done\n Time: {}\n".format(end_time - start_time)
