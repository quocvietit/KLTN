"""
@name: file_service.py
@author: Vuong Quoc Viet
@version: 1.0
@since: Feb 27, 2018
"""

from json import dump
from time import sleep
from random import random


class FileService:
    def __init__(self, file_path):
        self.__filePath = file_path

    def write(self, data=None, delay=0.1):
        while True:
            try:
                with open(self.__filePath + '.json', "w+") as f:
                    return dump(data, f, sort_keys = True, indent= 4)
            except Exception as ex:
                print ex
                sleep(random() * delay)

    def read(self, delay=0.1):
        while True:
            try:
                with open(self.__filePath, 'r') as f:
                    return f
            except Exception as ex:
                print ex
                sleep(random() * delay)
