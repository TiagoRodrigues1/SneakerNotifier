from src.BaseCaller import BaseCaller
from src.SneakerInfo import SneakerInfo

def getSneakers():
    baseUrl = "https://launches.endclothing.com/"
    
    baseCaller = BaseCaller(baseCaller, None)
    soup = baseCaller.getHtml()
    sneakers = []

    
