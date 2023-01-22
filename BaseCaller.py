# Created by Tiago on 05/01/2023
# This aims to be the base caller for the SneakerInfo bot
# Can parse a JSON request or just get the page scrapped

import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

class BaseCaller:

    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def getJson(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()

    def getHtml(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
        content = driver.page_source
        return BeautifulSoup(content, "html.parser")