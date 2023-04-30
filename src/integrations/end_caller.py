from src.BaseCaller import BaseCaller
from src.SneakerInfo import SneakerInfo
import numpy as np


def getSneakers():
    baseUrl = "https://launches-api.endclothing.com/api/products/offset/0"

    baseCaller = BaseCaller(baseUrl, None)
    json = baseCaller.getJson()
    sneakers = []

    products = json["products"]
    for sneaker in products:

        title = sneaker["brand"]
        subtitle = sneaker["name"]
        image = sneaker["thumbnailUrl"]
        releaseDate = sneaker["releaseDate"]

        prodPrices = sneaker["productWebsites"]

        for price in prodPrices:
            website = price["website"]
            if website["currencyCode"] == "EUR":
                currentPrice = price["price"]
                break

        sneakers.append(SneakerInfo(
            subtitle + " " + title, image, str(currentPrice) + "€", releaseDate))

    return sneakers
