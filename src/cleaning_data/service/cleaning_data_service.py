"""
@name: cleaning_data_service
@author: Vuong Quoc Viet
@version: 1.0
@since: Mar 03, 2018
"""
import json
from cleaning_data.service.file_service import FileService
from cleaning_data.service.mapper_service import MapperService
from cleaning_data.service.covert_json_service import ConvertJsonService


class CleaningDataService:
    def __init__(self, file_path, file_name, version):
        self.__filePath = file_path
        self.__fileName = file_name
        self.__version = version
        self.__fileOutput = FileService(self.__filePath + file_name[:-5] + "_" + self.__version)
        self.__mapper = MapperService()
        self.__covert = ConvertJsonService()

    def start(self):
        try:
            with open(self.__filePath + self.__fileName, 'r') as f:
                data = []
                while True:
                    line = f.readline()
                    if not line:
                        break
                    try:
                        object_data = self.__mapper.mapper(line)
                        json_data = self.__covert.get_json(object_data)
                        data.append(json.loads(json_data))
                    except Exception as ex:
                        print "Error load: ", ex

            self.__fileOutput.write(data)
        except Exception as ex:
            print "Error read: ", ex
