import requests

class BaseCaller:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def getJson(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()