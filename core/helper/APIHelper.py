import requests
import subprocess
import copy


from core.helper import CollectionHelper as collection
from core.helper import DictHelper as dictHelper
from core.helper.DataHelper import DataHelper as dataReader

"""
    Class to handle API requests.
    This class offer methods to do API request given an endpoints Collection
"""

DEFAULT_PATH = "./collections/CollectionsPaths.json"

class APIHelper(object):

    __instance = None
    __request = None
    __response = None

    def __init__(self):
        """
            Constructor
            If this constructor is called, It will raise a NotImplementedError

            :raise: NotImplementedError
        """
        raise RuntimeError('This is a Singlenton Class. Use getInstance() instead')

    @classmethod
    def getInstance(self):
        """
            Singleton Pattern to create an instance from APIHelper. 
            If the instance doesn't exist this method call to create it. Otherwise, It returns it.
            
            :return: APIHelper
        """
        if self.__instance is None:
            self.__instance = super(APIHelper,self).__new__(self)
        return self.__instance

    def getDataRequest(self, endpoint, dict):
        """
            Get API request data.

            :endpoint: is the name of endpoint in the collection file.
            :key: is the key to replace in environment file.
            :value: is the value to replace in environment file.

            This method reads :DEFAULT_PATH: file to find the way to the endpoint into collection.
            Calls the corresponding method to get endpoint data depending from :folders:.
            Also, replaces environments variables from environment file and replaces specific values from test
            located in :dict: param in collection data.

            :dict: is dynamic data. It could come from feature or another source. They are not obligatory.

            :raise: FileNotFoundError if :DEFAULT_PATH: is not found.
            :raise: Exception if an error occurred while getting endpoint data or 
                    the connection could not be established.

            :param endpoint_name: str
            :param dict: dict
            :return request: dict
        """
        try:
            dataReader.getInstance().setData(DEFAULT_PATH)
            folders = dataReader.getInstance().getData().get(endpoint.replace(" ", "_"))
        except FileNotFoundError as fnfe:
            raise fnfe

        try:
            if (folders):
                self.__request = collection.get_endpoint_data(endpoint,folders,dict)
            else:
                self.__request = collection.get_endpoint_data(endpoint,dict)
        except Exception as e:
            raise e
        return self.__request

    def doRequest(self):
        """
            Execute an API request.

            This method makes the request with data :__request: obtained from :getDataRequest: method
            and returns the response.

            :raise: Exception if an error occurred while getting endpoint data or 
                    the connection could not be established.

            :return response: dict
        """
        try:
            self.__response = requests.request(self.__request["method"], self.__request["url"],
                                               headers=self.__request["header"], data=self.__request["data"], auth=self.__request["auth"])
        except TypeError:
            raise TypeError(
                "Request data is not defined. First must be called the 'getDataRequest' function")
        except Exception as e:
            raise Exception("Unable to stablish connection with the service")

        return self.__response

    def doPrerequest(self):
        """
            Execute Pre request scripts.

            Runs the scripts specified in the events prerequest section of the collection.
            This :__request: is obtained from :getDataRequest: method.
            The scripts are in the folder :./scripts/: and update the environment variables in
            environment file defined in :./config.json: file.
        """
        try:
            if (self.__request.get("events").get("prerequest")):
                for e in self.__request.get("events").get("prerequest"):
                    subprocess.call(['python', './scripts/{}'.format(e)])
        except Exception as e:
            raise Exception(
                "An exception occurred while running the Pre-Request script")

    def doPostrequest(self):
        """
            Execute Post request scripts.

            Runs the scripts specified in the events test section of the collection.
            This :__request: is obtained from :getDataRequest: method.
            The scripts are in the folder :./scripts/: and update the environment variables in
            environment file defined in :./config.json: file.

            This method must be run after the doRequest method, as it needs the response from the service.
        """
        try:
            if (self.__request.get("events").get("test")):
                for e in self.__request.get("events").get("test"):
                    subprocess.call(
                        ['python', './scripts/{}'.format(e), self.getStringResponse()])
        except Exception as e:
            raise Exception(
                "An exception occurred while running the Post-Request script")

    def getStatusCode(self):
        """
            Return the current status code
            :return: int
        """
        return self.__response.status_code

    def getTimeElapsed(self):
        """
            Return the response time elapsed
            :return: int
        """
        return self.__response.elapsed.total_seconds

    def getRequest(self):
        """
            Return the current request as dict
            :return: dict
        """
        return self.hideCredentials()

    def getResponse(self):
        """
            Return the current response
            :return: dict/str
        """
        try:
            return self.__response.json()
        except Exception:
            return self.getStringResponse()

    def getStringResponse(self):
        """
            Return the current response as String
            :return: str
        """
        return self.__response.text

    def hideCredentials(self):
        """
            Return a copy of current request with the hidden credentials 
        """
        request = copy.deepcopy(self.__request)
        sensible_data = ["auth", "Authorization", "client_id", "client_secret", "secretkey", "url"]
        for s in sensible_data:
            dictHelper.hideKeyData(request, s)
        return request