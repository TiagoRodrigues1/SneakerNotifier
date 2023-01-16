from BaseCaller import BaseCaller
from SneakerInfo import SneakerInfo


def getSneakers():
    baseUrl = "https://api.nike.com/product_feed/threads/v3/?anchor=0&count=50&filter=marketplace%28PT%29&filter=language%28pt-PT%29&filter=upcoming%28true%29&filter=channelId%28010794e5-35fe-4e32-aaff-cd2c74f89d61%29&filter=exclusiveAccess%28true%2Cfalse%29&sort=effectiveStartSellDateAsc"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    baseCaller = BaseCaller(baseUrl, headers)
    jsonSneakers = baseCaller.getJson()
    sneakers = []

    for sneaker in jsonSneakers["objects"]:
        publishedContent = sneaker["publishedContent"]
        title = publishedContent["properties"]["coverCard"]["properties"]["title"]
        subtitle = publishedContent["properties"]["coverCard"]["properties"]["subtitle"]

        image = sneaker["publishedContent"]["nodes"][0]["nodes"][0]["properties"]["squarishURL"]
        merchPrice = sneaker["productInfo"][0]["merchPrice"]
        price = str(merchPrice["fullPrice"]) + merchPrice["currency"]
        releaseDate = sneaker["productInfo"][0]["launchView"]["startEntryDate"]


        sneakers.append(SneakerInfo(
            subtitle + " " + title, image, price, releaseDate))
    
    return sneakers
