import json, re

from requests_aws4auth import AWS4Auth
from requests.auth import HTTPBasicAuth
from core.helper.DataHelper import DataHelper as dataReader
from multipledispatch import dispatch


DEFAULT_PATH = "./collections"
CONFIG_JSON = "./config.json"

"""
    File to handle Postman collection data.
    This file provides static methods to get data from  json collection files.
"""

@dispatch(str, dict)
def get_endpoint_data(endpoint, dict={}):
    """
        Override method.
        This method takes :endpoint: param, search and return their data.
        Also, replaces environments variables from environment file and replaces specific values from test
        located in :dict: param in collection data.

        :raise: KeyError if :endpoint: is not present in collection.

        :param endpoint: str
        :param dict: dict
        :return: dict
    """
    collection = __get_collection()
    environment = __get_environment()
    items = collection["item"]
    for item in items:
        if item["name"] == endpoint:
            return __get_request_params(__format_collection(item,__format_environment(environment,dict))) # -> Format collection
    raise KeyError("Unable to find a endpoint called {} into collection file".format(endpoint))

@dispatch(str, list, dict)
def get_endpoint_data(endpoint, collection_folders, dict={}):
    """
        Override method.
        This method search the endpoint :endpoint: into path specified in :collection_folders: param
        and return their data.
        Also, replaces environments variables from environment file and replaces specific values from test
        located in :dict: param in collection data.

        :raise: KeyError if :endpoint: is not present in collection.

        :param endpoint: str
        :param collection_folders: list
        :param dict: dict
        :return: dict
    """
    collection = __get_collection()
    environment = __get_environment()
    items = __extract_data(collection["item"],collection_folders)
    for item in items:
        if item["name"] == endpoint:
            return __get_request_params(__format_collection(item,__format_environment(environment,dict)))
    raise KeyError("Unable to find a endpoint called {} into collection file".format(endpoint))

def __get_request_params(endpoint):
    """
        This method creates and returns a dictionary with all data necessary to make an API request.

        :param: str
        :return: dict
    """
    params = {}
    params["method"] = endpoint["request"]["method"]
    params["url"] = endpoint["request"]["url"]["raw"]
    params["header"] = __get_header_params(endpoint)
    params["data"] = __get_data_params(endpoint)
    params["auth"] = __get_auth_params(endpoint)
    params["events"] = __get_events(endpoint)
    return params

def __get_header_params(endpoint):
    """
        This method gets and returns from the collection all header data necessary to make an API request.

        :raise: KeyError if the collection hasn't got header entry.

        :param: str
        :return: dict
    """
    data = {}
    try:
        if (endpoint["request"]["header"]):
            headers = endpoint["request"]["header"]
            for header in headers:
                if (not header["key"] == ""):
                    data.update({header["key"]:header["value"]})
    except KeyError as ke:
        raise KeyError("An error has occurred while read header params")                 
    return data

def __get_data_params(endpoint):
    """
        This method gets and returns from the collection all body data necessary to make an API request.

        :raise: NotImplementedError if the "body mode" entry is different to "formdata" or "urlencoded".
        :raise: KeyError if the collection hasn't got any body entry.

        :param: str
        :return: dict
    """
    data = {}
    body = endpoint.get("request").get("body")
    if (body):
        try:
            if (body["mode"] == "formdata"):
                body_params = body["formdata"]
            elif (body["mode"] == "urlencoded"):
                body_params = body["urlencoded"]
            elif (body["mode"] == "raw"):
                if (body["options"]["raw"]["language"] == "json"):
                    return json.dumps(body["raw"])
                else:
                    raise NotImplementedError("Body languaje mode is not supported")
            else:
                raise NotImplementedError("Body mode is not supported")
            for param in body_params:
                data.update({param["key"]:param["value"]})
        except KeyError as ke:
            raise KeyError("An error has occurred while read body data params") 
    return data

def __get_auth_params(endpoint):
    """
        This method gets and returns from the collection all auth data necessary to make an API request.

        :raise: NotImplementedError if the "type" auth entry is different to "awsv4".
        :raise: KeyError if the collection hasn't got the keys with the same names.

        :param: str
        :return: empty dict if hasn't got auth entry or AWS4Auth type object.
    """
    data = {}
    if (endpoint.get("request").get("auth")):
        auth = endpoint["request"]["auth"]
        if (auth.get("type") == "awsv4"):
            for i in auth["awsv4"]:
                data.update({i["key"]:i["value"]})
            try:
                return AWS4Auth(data["accessKey"],data["secretKey"],data["region"],data["service"])
            except KeyError as ke:
                raise KeyError("An error has occurred while read AWS auth params")
        if (auth.get("type") == "basic"):
            for i in auth["basic"]:
                data.update({i["key"]:i["value"]})
            try:
                return HTTPBasicAuth(data["username"],data["password"])
            except KeyError as ke:
                raise KeyError("An error has occurred while read Basic auth params")
        else:
            raise NotImplementedError("Type of authentication is not valid")
    return data


def __get_events(endpoint):
    """
        This method gets and returns from the collection all event data necessary to make the preconditions
        or post conditions of an API request.

        :raise: KeyError if the collection hasn't got the keys with the same names.

        :param: str
        :return: empty dict if hasn't got auth entry or AWS4Auth type object.
    """
    data = {}
    if (endpoint.get("event")):
        event = endpoint["event"]
        for e in event:
            try:
                data.update({e["listen"]:e["script"]["exec"]})
            except KeyError as ke:
                raise KeyError("An error has occurred while read event params")
    return data

            
def __get_collection():
    """
        This method obtains from :CONFIG_JSON: file the name of the collection file and
        from :DEFAULT_PATH: the path to him. Reads and return these data.

        :raise: KeyError if "postmanCollection" entry doesn't exist in :CONFIG_JSON: file.
        :raise: FileNotFoundError if any file (CONFIG_JSON or collection file) doesn't exist.

        :return: dict
    """
    dataReader.getInstance().setData(CONFIG_JSON)
    params = dataReader.getInstance().getData()
    try:
        collection_file = "{}/{}".format(DEFAULT_PATH,params["postmanCollection"])
        dataReader.getInstance().setData(collection_file)
        return dataReader.getInstance().getData()
    except KeyError as ke:
        raise KeyError("Unable to find the attribute 'postmanCollection' into config.json")
    except FileNotFoundError as fnfe:
        raise fnfe

def __get_environment():
    """
        This method obtains from :CONFIG_JSON: file the name of the environment file and
        from :DEFAULT_PATH: the path to him. Reads and return these data.

        :raise: KeyError if "postmanEnvironment" entry doesn't exist in :CONFIG_JSON: file.
        :raise: FileNotFoundError if any file (CONFIG_JSON or environment file) doesn't exist.

        :return: dict
    """
    dataReader.getInstance().setData(CONFIG_JSON)
    params = dataReader.getInstance().getData()
    try:
        environment_file = "{}/{}".format(DEFAULT_PATH,params["postmanEnvironment"])
        dataReader.getInstance().setData(environment_file)
        return dataReader.getInstance().getData()
    except KeyError as ke:
        raise KeyError("Unable to find the attribute 'postmanEnvironment' into config.json")
    except FileNotFoundError as fnfe:
        raise fnfe
    
def __format_environment(environment, dict):
    """
        This method replace data of environment file with dinamic data from test.

        :raise: KeyError if any key ("key", "values", "emabled") is not present in environment object.
        :raise: TypeError if :dict: is not of type :dict:. :D

        :param environment: dict of data read from environment file
        :param dict: dict with keys and values to replace in :enviroment: from test

        :return: dict of environment data formatted with params from test
    """
    data = {}   
    try:
        for e in environment['values']:
            if e['enabled']:
                data.update({e["key"]:e["value"]})
        for key, value in dict.items():
            if key in data:
                data.update({key:value})
    except TypeError:
        raise TypeError("'dict' param must be of type :dict:")
    except KeyError:
        raise KeyError("An error has occurred while read environment data") 
    return data


def __update_environment(environment, dict):
    """
        This method update data of environment file with dinamic data from another request.

        :raise: KeyError if any key ("key", "values", "emabled") is not present in environment object.
        :raise: TypeError if :dict: is not of type :dict:. :D

        :param environment: dict of data read from environment file
        :param dict: dict with keys and values to replace in :enviroment: from another request

        :return: dict of environment data update with params from another request
    """
    try:
        for k, v in dict.items():
            e = next((item for item in environment["values"] if item["key"] == k), None)
            if (e != None):
                e["value"] = dict[e["key"]]
            else:
                environment["values"].append({"key":k, "value":v, "enabled":True})
    except TypeError:
        raise TypeError("'dict' param must be of type :dict:")
    except KeyError:
        raise KeyError("An error has occurred while update environment data") 
    return environment


def __format_collection(collection, env):
    """
        This method replace data of environment file (formatted with data from test) in collection data

        :raise KeyError: if any key from environment file is not present in collection data

        :param collection: dict of data read from collection file
        :param env: dict of data read from environment file

        :return: dict of collection data formatted with params from environment data
    """
    if isinstance(collection, str):
        try:
            if re.sub('[{}]','',collection) in env:
                return env[re.sub('[{}]','',collection)]
            else:
                return collection.replace('{{', '{').replace('}}', '}').format(**env).format(**env)
        except KeyError as e:
            raise KeyError("Except value {} in environment variables. Environment variables are {}".format(e, env))
    elif isinstance(collection, dict):
        return __format_dict(collection, env)
    elif isinstance(collection, list):
        return [__format_collection(oo, env) for oo in collection]
    elif isinstance(collection, object):
        return collection


def __format_dict(d, env):
    """
        Auxiliar method to replace environment data in collection data

        :param d: dict
        :param env: dict of data read from environment file

        :return: dict formatted with params from environment data
    """
    kwargs = {}
    for k, v in d.items():
        kwargs[k] = __format_collection(v, env)
    return kwargs

def __extract_data(items, folders):
    """
        Recursive method to get endpoint data located into subfolders of the collection.

        :raise: AttributeError if :folders: param isn't a list.
        :raise: KeyError if any folder in :folders: is not present in :items: collection.

        :param items: dict
        :param folders: list
        :return endpoint_data: dict 
    """
    for item in items :
        if (item["name"] == folders[0]):
            if len(folders) == 1:
                return item["item"]
            elif len(folders) > 1:
                items = item["item"]
                folders.pop(0)
                return __extract_data(items,folders)
            else:
                raise AttributeError("The attribute folders must be a List")
    raise KeyError("Unable to find item")