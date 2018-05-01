import requests

URL = 'https://api.exmo.com/v1/'
valytu = {'zec': 'ZEC_USD', 'eth': 'ETH_USD', 'bch': 'BCH_USD', 'xrp': 'XRP_USD', 'etc': 'ETC_USD'}
#k = ['ZEC_USD', 'ETH_USD', 'BCH_USD', 'XRP_USD', 'ETC_USD']
interests_could_be = ['buy_price', 'sell_price', 'vol', 'avg']
upd = 0

def get_usd(obj, interest):
    url = URL + 'ticker/'
    r = requests.get(url)
    data = r.json()

    info_all = data[obj]
    #     ast.literal_eval(json.dumps(info_all))
    result = info_all[interest]
    return '{} of {}: {} USD'.format(interest, obj, result)

# for i in interests_could_be:
#     for j in k:
#         print(get_usd(j, i))
#     print()