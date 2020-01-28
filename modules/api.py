import requests
from typing import Union
from json.decoder import JSONDecodeError


class ApiRequestError(Exception):
    def __init__(self):
        self.message = "Server could not answer the request."


class GeometryDashApi:
    apiUrl = "https://gdbrowser.com"

    def __request(self, method: str, relatUrl: str, data: dict=None, rawFile: bool=False):
        if method == "get":
            result = requests.get(self.apiUrl + relatUrl, params=data)
        elif method == "post":
            result = requests.post(self.apiUrl + relatUrl, data=data)
        else:
            raise NotImplementedError()

        if rawFile:
            from io import BytesIO
            return BytesIO(result.content)

        if result.text == "-1":
            raise ApiRequestError()
        try:
            return result.json()
        except (ValueError, JSONDecodeError):
            return result.text


    def getLevel(self, levelId: int, download: bool=False):
        params = {'download': True if download else None}
        return self.__request("get", "/api/level/{}".format(levelId), params)

    def getProfile(self, userId: Union[int, str]):
        return self.__request("get", "/api/profile/{}".format(userId))

    def parseLevel(self, levelId: int):
        return self.__request("get", "/api/analyze/{}".format(levelId))

    def getIcon(self, username: str, form: str="cube"):
        params = {'form': form}
        return self.__request("get", "/icon/{}".format(username), params, rawFile=True)

    def createIcon(self, form: str="cube", icon: int=0, col1: int=0, col2: int=0, glow: bool=False):
        params = {'form': form, 'icon': icon,
                  'col1': col1, 'col2': col2,
                  'glow': 0 if glow is False else 1}
        return self.__request("get", "/icon/new", params, rawFile=True)
