from BaseCaller import BaseCaller
from SneakerInfo import SneakerInfo


def getSneakers():
    baseUrl = "https://www.sneakersnstuff.com/en/937/sns-sign-up"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    baseCaller = BaseCaller(baseUrl, headers)
    soup = baseCaller.getHtml()
    sneakers = []

    for sneaker in soup.findAll(attrs={'class': 'card product'}):
        brand = sneaker.find(attrs={'class': 'card__brand'}).text.strip()
        name = sneaker.find(attrs={'class': 'card__name'}).text.strip()
        price = sneaker.find(attrs={'class': 'price'}).text.strip()
        img = sneaker.find('img').get('src')
        releaseDate = sneaker.find(
            attrs={'class': 'countdown card__countdown release-date'}).get('datetime')

        sneakers.append(SneakerInfo(
            brand + " " + name, img, price, releaseDate))
        

    return sneakers
