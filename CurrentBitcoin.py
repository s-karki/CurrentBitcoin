import urllib.request
import json



class CurrentBitCoin:
    def __init__(self):
        raw = self.getRawData()
        priceDict = self.process(raw)
        self.time = priceDict["time"]
        self.USD = priceDict["USD"]
        self.GBP = priceDict["GBP"]
        self.EUR = priceDict["EUR"]


    def getRawData(self):
        request = urllib.request.urlopen("http://api.coindesk.com/v1/bpi/currentprice.json")
        response = request.read().decode('utf-8')
        rawjson = json.loads(response)
        return rawjson

    def process(self,rawjson):
        priceDict = {}
        coinPrice = rawjson["bpi"]
        coinTime = rawjson["time"]["updatedISO"]
        priceDict['time'] = coinTime
        for x in coinPrice:
            priceDict[x] = coinPrice[x]["rate"]
        return(priceDict)

    def getCurrencyPrice(self, code):
        request = urllib.request.urlopen("http://api.coindesk.com/v1/bpi/currentprice/{}.json".format(code))
        response = request.read().decode('utf-8')
        rawjson = json.loads(response)
        priceDict = {}
        priceDict['time'] = rawjson["time"]["updatedISO"]
        coinPrice = rawjson["bpi"][code]["rate"]
        return coinPrice












