import sys
sys.path.append('../PyServer')

from MQLServer import *

def ToBool(x): return int(x)==1
def OrderClose(ticket, lots, price, slippage, Color):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderClose("+repr(ticket)+", "+repr(lots)+", "+repr(price)+", "+repr(slippage)+", "+repr(Color)+" )")
    if ApiAdapter.debug:print "OrderClose->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def OrderSend(symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment, magic, expiration, arrow_color):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderSend("+symbol+", "+repr(cmd)+", "+repr(volume)+", "+repr(price)+", "+repr(slippage)+", "+repr(stoploss)+", "+repr(takeprofit)+", "+comment+", "+repr(magic)+", "+repr(expiration)+", "+repr(arrow_color)+" )")
    if ApiAdapter.debug:print "OrderSend->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderModify(ticket, price, stoploss, takeprofit, expiration, arrow_color):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderModify("+repr(ticket)+", "+repr(price)+", "+repr(stoploss)+", "+repr(takeprofit)+", "+repr(expiration)+", "+repr(arrow_color)+" )")
    if ApiAdapter.debug:print "OrderModify->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def AccountBalance():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:AccountBalance()")
    if ApiAdapter.debug:print "AccountBalance->",ret
    retval=float(ret[4:].strip())
    return retval
def AccountCredit():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:AccountCredit()")
    if ApiAdapter.debug:print "AccountCredit->",ret
    retval=float(ret[4:].strip())
    return retval
def AccountCompany():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:AccountCompany()")
    if ApiAdapter.debug:print "AccountCompany->",ret
    retval=""+(ret[4:].strip())
    return retval
def AccountCurrency():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:AccountCurrency()")
    if ApiAdapter.debug:print "AccountCurrency->",ret
    retval=""+(ret[4:].strip())
    return retval
def MathLog(x):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:MathLog("+repr(x)+" )")
    if ApiAdapter.debug:print "MathLog->",ret
    retval=float(ret[4:].strip())
    return retval
def MarketInfo(symbol, type):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:MarketInfo("+symbol+", "+repr(type)+" )")
    if ApiAdapter.debug:print "MarketInfo->",ret
    retval=float(ret[4:].strip())
    return retval
def iBars(symbol, timeframe):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iBars("+symbol+", "+repr(timeframe)+" )")
    if ApiAdapter.debug:print "iBars->",ret
    retval=int(ret[4:].strip())
    return retval
def iOpen(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iOpen("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iOpen->",ret
    retval=float(ret[4:].strip())
    return retval
def iClose(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iClose("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iClose->",ret
    retval=float(ret[4:].strip())
    return retval
def iHigh(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iHigh("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iHigh->",ret
    retval=float(ret[4:].strip())
    return retval
def iLow(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iLow("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iLow->",ret
    retval=float(ret[4:].strip())
    return retval
def iTime(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iTime("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iTime->",ret
    retval=float(ret[4:].strip())
    return retval
def iVolume(symbol, timeframe, shift):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iVolume("+symbol+", "+repr(timeframe)+", "+repr(shift)+" )")
    if ApiAdapter.debug:print "iVolume->",ret
    retval=float(ret[4:].strip())
    return retval
def iBarShift(symbol, timeframe, time, exact):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:iBarShift("+symbol+", "+repr(timeframe)+", "+repr(time)+", "+repr(exact)+" )")
    if ApiAdapter.debug:print "iBarShift->",ret
    retval=int(ret[4:].strip())
    return retval
def OrdersTotal():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrdersTotal()")
    if ApiAdapter.debug:print "OrdersTotal->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderLots():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderLots()")
    if ApiAdapter.debug:print "OrderLots->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderSelect(index, select):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderSelect("+repr(index)+", "+repr(select)+" )")
    if ApiAdapter.debug:print "OrderSelect->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def GetLastError():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:GetLastError()")
    if ApiAdapter.debug:print "GetLastError->",ret
    retval=int(ret[4:].strip())
    return retval
def HistoryTotal():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:HistoryTotal()")
    if ApiAdapter.debug:print "HistoryTotal->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderCommission():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderCommission()")
    if ApiAdapter.debug:print "OrderCommission->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderExpiration():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderExpiration()")
    if ApiAdapter.debug:print "OrderExpiration->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderMagicNumber():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderMagicNumber()")
    if ApiAdapter.debug:print "OrderMagicNumber->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderOpenPrice():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderOpenPrice()")
    if ApiAdapter.debug:print "OrderOpenPrice->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderProfit():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderProfit()")
    if ApiAdapter.debug:print "OrderProfit->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderStopLoss():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderStopLoss()")
    if ApiAdapter.debug:print "OrderStopLoss->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderSwap():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderSwap()")
    if ApiAdapter.debug:print "OrderSwap->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderTakeProfit():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderTakeProfit()")
    if ApiAdapter.debug:print "OrderTakeProfit->",ret
    retval=float(ret[4:].strip())
    return retval
def OrderType():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderType()")
    if ApiAdapter.debug:print "OrderType->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderTicket():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderTicket()")
    if ApiAdapter.debug:print "OrderTicket->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderSymbol():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderSymbol()")
    if ApiAdapter.debug:print "OrderSymbol->",ret
    retval=""+(ret[4:].strip())
    return retval
def IsConnected():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsConnected()")
    if ApiAdapter.debug:print "IsConnected->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsDemo():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsDemo()")
    if ApiAdapter.debug:print "IsDemo->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsDllsAllowed():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsDllsAllowed()")
    if ApiAdapter.debug:print "IsDllsAllowed->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsLibrariesAllowed():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsLibrariesAllowed()")
    if ApiAdapter.debug:print "IsLibrariesAllowed->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsStopped():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsStopped()")
    if ApiAdapter.debug:print "IsStopped->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsTesting():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsTesting()")
    if ApiAdapter.debug:print "IsTesting->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def IsTradeAllowed():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:IsTradeAllowed()")
    if ApiAdapter.debug:print "IsTradeAllowed->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def RefreshRates():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:RefreshRates()")
    if ApiAdapter.debug:print "RefreshRates->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def HaveTicks():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:HaveTicks()")
    if ApiAdapter.debug:print "HaveTicks->",ret
    retval=ToBool(ret[4:].strip())
    return retval
def ActsPerTick(val):
    ret=ApiAdapter.instance.ForwardToMQL("FUN:ActsPerTick("+repr(val)+" )")
    if ApiAdapter.debug:print "ActsPerTick->",ret
    retval=int(ret[4:].strip())
    return retval
def OrderCloseTime():
    ret=ApiAdapter.instance.ForwardToMQL("FUN:OrderCloseTime()")
    if ApiAdapter.debug:print "OrderCloseTime->",ret
    retval=float(ret[4:].strip())
    return retval
