import json
from unicodedata import name
from urllib.request import urlopen

link2 = "https://api.hypixel.net/resources/skyblock/items"
resp2 = urlopen(link2)
data2 = json.loads(resp2.read())

link1 = "https://api.hypixel.net/skyblock/auctions"
resp = urlopen(link1)
data1 = json.loads(resp.read())

prices = {
}

for i in data2["items"]:
    if "npc_sell_price" in i.keys():
        prices[i["name"]] = i["npc_sell_price"]

for i in data1["auctions"]:
    if i["item_name"] in prices.keys():
        if i["starting_bid"] < prices[i["item_name"]]:
            print(i["item_name"])


    
