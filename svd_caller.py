from BaseCaller import BaseCaller
from SneakerInfo import SneakerInfo


def getSneakers():
    url = "https://www.sivasdescalzo.com/graphql?query=query%20categoryV4(%24id%3A%20Int!%2C%20%24pageSize%3A%20Int!%2C%20%24currentPage%3A%20Int!%2C%20%24filters%3A%20ProductAttributeFilterInput!%2C%20%24sort%3A%20ProductAttributeSortInput)%20%7B%0A%20%20currency%3A%20currency%20%7B%0A%20%20%20%20default_display_currency_symbol%0A%20%20%20%20__typename%0A%20%20%7D%0A%20%20category(id%3A%20%24id)%20%7B%0A%20%20%20%20name%0A%20%20%20%20__typename%0A%20%20%7D%0A%20%20products(pageSize%3A%20%24pageSize%2C%20currentPage%3A%20%24currentPage%2C%20filter%3A%20%24filters%2C%20sort%3A%20%24sort)%20%7B%0A%20%20%20%20items%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%20%20brand_name%0A%20%20%20%20%20%20name%0A%20%20%20%20%20%20sku%0A%20%20%20%20%20%20small_image%20%7B%0A%20%20%20%20%20%20%20%20url%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20url%0A%20%20%20%20%20%20original_price%0A%20%20%20%20%20%20original_price_formatted%0A%20%20%20%20%20%20final_price%0A%20%20%20%20%20%20final_price_formatted%0A%20%20%20%20%20%20percent_off%0A%20%20%20%20%20%20state%0A%20%20%20%20%20%20badge%0A%20%20%20%20%20%20has_promotion%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20aggregations%20%7B%0A%20%20%20%20%20%20attribute_code%0A%20%20%20%20%20%20label%0A%20%20%20%20%20%20count%0A%20%20%20%20%20%20options%20%7B%0A%20%20%20%20%20%20%20%20label%0A%20%20%20%20%20%20%20%20value%0A%20%20%20%20%20%20%20%20count%0A%20%20%20%20%20%20%20%20__typename%0A%20%20%20%20%20%20%7D%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20page_info%20%7B%0A%20%20%20%20%20%20total_pages%0A%20%20%20%20%20%20__typename%0A%20%20%20%20%7D%0A%20%20%20%20total_count%0A%20%20%20%20__typename%0A%20%20%7D%0A%7D%0A&operationName=categoryV4&variables=%7B%22currentPage%22%3A1%2C%22id%22%3A4006%2C%22filters%22%3A%7B%22category_id%22%3A%7B%22eq%22%3A%224006%22%7D%7D%2C%22pageSize%22%3A64%2C%22sort%22%3A%7B%22sorting_date%22%3A%22DESC%22%7D%7D"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    baseCaller = BaseCaller(url, headers)
    responseJson = baseCaller.getJson()
    sneakers = []

    for prodcut in responseJson["data"]["products"]["items"]:
        brandName = prodcut["brand_name"]
        name = prodcut["name"]
        price = str(prodcut["final_price"]) + "EUR"
        date = prodcut["state"]
        img = ""

        sneakers.append(SneakerInfo(
            brandName + " " + name, img, price, date))

    return sneakers
