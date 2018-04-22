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


def get_version():
    date = datetime.datetime.now()
    day = str(date.day) if date.day >= 10 else "0" + str(date.day)
    month = str(date.month) if date.month >= 10 else "0" + str(date.month)
    year = str(date.year)

    return day + month + year


if __name__ == '__main__':
    path = '../data/'
    pages = ['bbcnews',
             'VOATiengViet',
             'voiceofamerica']
    years = ['2012',
             '2013',
             '2014',
             '2015',
             '2016',
             '2017']
    version = get_version()

    start_time = datetime.datetime.now()
    print("Start: {}".format(start_time))

    for page in pages:
        for year in years:
            file = page + '_posts_' + year + '.json'
            clean(path, file, version)

    end_time = datetime.datetime.now()
    print "Done\n Time: {}\n".format(end_time - start_time)
