#https://docs.ccxt.com/en/latest/manual.html

import ccxt
import jsonparse

exchange = ccxt.binance()


def CalcularVariacao(nomePar):
  par = jsonparse.objJson(exchange.fetch_ticker(nomePar))
  dif = par.high - par.low
  por = (dif * 100) / par.low

  print (nomePar)
  print ("H: " + str(par.high))
  print ("L: " + str(par.low))
  print ("D: " + str(dif))
  print ("%: " + str(por))
  print ()

CalcularVariacao("BTC/USDT")
CalcularVariacao("SOL/USDT")
CalcularVariacao("APE/USDT")
CalcularVariacao("UNFI/USDT")