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

def sell_btc(amount, price):
	order = api.place_order(book='btc_mxn', side='sell', order_type='limit', major=amount, price=price)

bitso_status()
print("Colocando orden de venta de bitcoins...")
sell_btc(amount='0.00104165', price='90000.00')
print("Orden colocada")
bitso_status()