"""
@name: file_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Jan 31, 2018
"""
#!/usr/bin/python
# coding=utf-8
from json import dump
from time import sleep
from random import random


class FileService:
    def __init__(self, file_path):
        self.__filePath = file_path

    def write(self, data=None, delay=0.1):
        while True:
            try:
                with open(self.__filePath+'.json', "ab+") as f:
                    return dump(data, f)
            except Exception as ex:
                print ex
                sleep(random() * delay)

