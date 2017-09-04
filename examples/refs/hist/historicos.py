"""
Obtener:
Precio USD en MXN segun fecha
#Obtener valor inmediato anterior si date no se encuentra
def precioUSD_MXN(qtyUSD, date) 

#Valor inmediato anterior si date no se encuentra
#Regresa lista de precios de dicho dia
#Considera precios como precios de venta de BTC (Cambiar USD a BTC)
#Encontrar maximos por dia
#Encontrar minimos por dia
#Cotizar en base a BTC disponibles para cierto precio (No vende los BTC a menos que haya suficientes a x precio)
def precioBTC_USD(qtyBTC, date) 
"""

import csv
from datetime import datetime as dt
from datetime import timedelta as td
mxn_prices = []

def get_mxn_prices():
	with open('MXN_USD_14-17.csv', 'r') as f:
		reader = csv.reader(f)
		mxn_list = list(reader)
		mxn_date_prices = {dt.strptime(price[0], "%d/%m/%Y"): float(price[1]) for price in mxn_list}
		return mxn_date_prices

mxn_prices = get_mxn_prices()

def get_mxn_by_date(date):
	global mxn_prices
	assert date >= dt(2014, 1, 2, 0, 0), "data starts at 02/01/2014"
	assert date <= dt(2017, 9, 1, 0, 0), "data ends at 09/02/2017"
	d = dt(date.year, date.month, date.day, 0, 0)
	while not d in mxn_prices:
		d = d - td(days=1)
	return mxn_prices[d]
	
