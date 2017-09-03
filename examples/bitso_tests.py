print("BITSO API TESTS")
import bitso
from btc_apikeys import *

api = bitso.Api(API_KEY, API_SECRET)

ob = api.order_book('btc_mxn')

def btc_update():
	ob = api.order_book('btc_mxn')

def btc_price():
	return min([float(ask.price) for ask in ob.asks])

def bitso_status():
	status = api.account_status()
	print("Daily limit=		{}".format(status.daily_limit))
	print("Daily remaining=	{}".format(status.daily_remaining))

bitso_status()