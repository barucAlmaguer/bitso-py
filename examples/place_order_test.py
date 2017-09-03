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

def place_order_btc(side, amount, price):
	print("Colocando orden de venta de bitcoins...")
	order = api.place_order(book='btc_mxn', side=side, order_type='limit', major=amount, price=price)
	print("Orden colocada")

def view_orders():
	oo = api.open_orders('btc_mxn')
	if len(oo) > 0:
		for o in oo:
			print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
			print("Order #:  {}".format(o.oid))
			print("\tSide=   {}".format(o.side))
			print("\tAmount= BTC${}".format(o.original_amount))
			print("\tPrice=  MXN${}".format(o.price))
		print("-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.")
	else:
		print("No current orders")

def cancel_order(oid):
	return api.cancel_order(oid)
		
def cancel_all_orders():
	oo = api.open_orders('btc_mxn')
	if len(oo) > 0:
		for o in oo:
			success = cancel_order(o.oid)
			if success:
				print("Order #{} cancelled".format(o.oid))
			else:
				print("Error cancelling order #{}".format(o.oid))
	else:
		print("No orders to cancel")
	
#place_order_btc(side='sell', amount='0.00104165', price='90000.00')