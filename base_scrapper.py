import  urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import time



class SneakerInfo:
    def __str__(self):
        return 'Sneaker -> ' + self.name + " with price -> " + self.price + " will be launched " + self.releaseDate
 
    def __init__(self, name, img, price, releaseDate):
        self.name = name
        self.img = img
        self.price = price
        self.releaseDate = releaseDate


baseUrl = "https://www.nike.com"
url = baseUrl + "/launch?s=upcoming"
headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}

#get the html
r = urllib.request.Request(url, data=None)
f = urllib.request.urlopen(r)
page = f.read().decode('utf-8')
soup = BeautifulSoup(page, "html.parser")

sneakers = []
links = []
dates = []

#get the href so we can go to each of the shoes links
for link in soup.find_all(attrs= {'data-qa':'product-card-link'}):
    links.append(link.get('href'))

for img in soup.find_all('img'):
    imgSrc = img.get('src')
    if(imgSrc.startswith("https://secure-images.nike.com/is/image/DotCom/")):
        links.append(imgSrc)
        print(imgSrc)


for dateM, dateday in zip(soup.find_all(attrs={'data-qa': 'test-startDate'}),soup.find_all(attrs = {'data-qa':'test-day'})):
    date = dateday.get_text() + " "+  dateM.get_text() + " 2023"
    dates.append(date)

#go through all the shoes and get the needed information
for idx, link in enumerate(links):
    r = urllib.request.Request(baseUrl + link, data=None)
    f = urllib.request.urlopen(r)
    page = f.read().decode('utf-8')
    soupSneaker = BeautifulSoup(page, "html.parser")
    print(baseUrl + link)
    name = soupSneaker.find(attrs={'class': 'headline-5=small'}).get_text()
    title = soupSneaker.find(attrs={'data-qa': 'product-title'}).get_text()
    price = soupSneaker.find(attrs={'data-qa': 'price'}).get_text()
    print(name)
    sneakers.append(SneakerInfo(name + title, links[idx], price, dates[idx]))
    time.sleep(5)
    
print(sneakers[0].__str__())

