import json, os
   
"""
    Singleton class to get parameters from data files.
    This class provides methods to read data from external files and feed test cases 
"""
class DataHelper(object):
    __instance = None
    __file = None
    #Singleton
    def __jsonDataReader(self, dataFile):
        """
            Loads all data from 'datafile' parameter and return as JSON format
            The parameter must contains the path to file, filename and extension
        """
        path = dataFile
        if os.path.exists(path):
            with open(path, encoding='utf-8') as data:
                return json.load(data)
        else:
            raise FileNotFoundError("Unable to find the file {}".format(path))

    def __linesDataReader(self, dataFile):
        """
            Loads all data from 'datafile' parameterand returns them line by line
            The parameter must contains the path to file, filename and extension
        """
        path = dataFile
        if os.path.exists(path):
            with open(file=path, mode='r', encoding='utf-8') as data:
                return data.readlines()
        else:
            raise FileNotFoundError("Unable to find the file {}".format(path))

    def __init__(self):
        raise RuntimeError('Use getInstance() instead')

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = super(DataHelper,cls).__new__(cls)
        return cls.__instance
    
    @DeprecationWarning
    def setDataName(self, name):
        self.__file = self.__jsonDataReader(name)

    def setData(self, name, type="json"):
        """
            Method to implement singleton pattern.
            Invokes the corresponding method depending on the 'type' parameter.

            :raise: NotImplementedError if 'type' is not supported.

            :param name: file path.
            :param type: read type. 'json' by default. At moment, only supports 'json' or 'line'.
        """
        if (type == "json"):
            self.__file = self.__jsonDataReader(name)
        elif (type == "line"):
            self.__file = self.__linesDataReader(name)
        else:
            raise NotImplementedError("Type {} is not implemented yet. Try with 'json' or 'line'".format(type))

    def getData(self):
        return self.__file

    def getDataLineByLine(self,name):
        return self.__linesDataReader(name)

    def getDataJson(self,name):
        return self.__jsonDataReader(name)

    def writeData(self,path,data):
        with open(file=path, mode='w', encoding='utf-8') as file:
            file.write(data)
            file.close()