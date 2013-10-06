
double NStrToDouble( string s)
{
   double ret;
   int digs=4;
   ret=StrToDouble(s);
   ret=NormalizeDouble(ret,digs);
   return (ret);
}
int _Errno=0;
int MGetLastError(int reset=1)
{
   if(reset==1)      _Errno=0;
   if(_Errno==0)  _Errno=GetLastError();
   return (_Errno);
}
        
string FunCall(string message)
{
   if (getDebug())
   Log("FunCall:"+message);
       {
        int index=0;
        int lindex=0;
        int argc=0;
        //string message;
        string FuncName;
        string Args[100];
        string ret;

	     lindex=index;
	     //search for function name
        index=StringFind(message,"(",lindex);
        if (index<0)
        {
            Log("Malformed message, cannot find function name");
        }
        //collect func name        
        FuncName=StringSubstr(message,lindex,index-lindex);
        if (getDebug()) Log("FuncName="+FuncName+" LastError: "+MGetLastError());
        lindex=index+1;
        //find first argument        
	     //now loop through them
        while( index > 0 ){
                index=StringFind(message,",",lindex);
                //Only one argument
                if (index==-1)
                {
                     index=StringFind(message,")",lindex);
                     if(index==-1)break;
                     Args[argc]=StringSubstr(message,lindex,index-lindex);
                     if(getDebug())
                           Log("E->"+StringSubstr(message,lindex,index-lindex)+" LastError: "+MGetLastError());
                     argc=argc+1;
                     break;           
               }
               else
               {
                  //found, advance left index
                  Args[argc]=StringSubstr(message,lindex,index-lindex);
                  argc=argc+1;
                  if(getDebug())
                       Log("N->"+StringSubstr(message,lindex,index-lindex)+" LastError: "+MGetLastError());
                  lindex=index+1 ;
               }
         }
     }
     Log("found "+argc+"arguments"+" LastError: "+MGetLastError());
     index=0;
     while(index<argc)
     {
      Log("Args:"+index+" "+Args[index]+" LastError: "+MGetLastError());
      index++;
     }
     index=0;
     if(getDebug()) 
         Log(FuncName+" "+MGetLastError());
      
	if (FuncName=="OrderClose") {
		bool retOrderClose;
		int ticket;
		double lots;
		double price;
		int slippage;
		color Color=CLR_NONE;
	
		index=0;
		ticket= StrToInteger(Args[index]);
		index++;
		lots= NStrToDouble(Args[index]);
		index++;
		price= NStrToDouble(Args[index]);
		index++;
		slippage= StrToInteger(Args[index]);
		index++;
		Color= StrToInteger(Args[index]);
		index++;
	
		retOrderClose=OrderClose(ticket, lots, price, slippage, Color);
		ret="RET:"+retOrderClose;
	}

	if (FuncName=="OrderSend") {
		int retOrderSend;
		string symbol;
		int cmd;
		double volume;
		double stoploss;
		double takeprofit;
		string comment=NULL;
		int magic=0;
		datetime expiration=0;
		color arrow_color=CLR_NONE;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		cmd= StrToInteger(Args[index]);
		index++;
		volume= NStrToDouble(Args[index]);
		index++;
		price= NStrToDouble(Args[index]);
		index++;
		slippage= StrToInteger(Args[index]);
		index++;
		stoploss= NStrToDouble(Args[index]);
		index++;
		takeprofit= NStrToDouble(Args[index]);
		index++;
		comment= ""+(Args[index]);
		index++;
		magic= StrToInteger(Args[index]);
		index++;
		expiration= NStrToDouble(Args[index]);
		index++;
		arrow_color= StrToInteger(Args[index]);
		index++;
	
		retOrderSend=OrderSend(symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment, magic, expiration, arrow_color);
		ret="RET:"+retOrderSend;
	}

	if (FuncName=="OrderModify") {
		bool retOrderModify;
		datetime expiration;
	
		index=0;
		ticket= StrToInteger(Args[index]);
		index++;
		price= NStrToDouble(Args[index]);
		index++;
		stoploss= NStrToDouble(Args[index]);
		index++;
		takeprofit= NStrToDouble(Args[index]);
		index++;
		expiration= NStrToDouble(Args[index]);
		index++;
		arrow_color= StrToInteger(Args[index]);
		index++;
	
		retOrderModify=OrderModify(ticket, price, stoploss, takeprofit, expiration, arrow_color);
		ret="RET:"+retOrderModify;
	}

	if (FuncName=="AccountBalance") {
		double retAccountBalance;
	
		retAccountBalance=AccountBalance();
		ret="RET:"+retAccountBalance;
	}

	if (FuncName=="AccountCredit") {
		double retAccountCredit;
	
		retAccountCredit=AccountCredit();
		ret="RET:"+retAccountCredit;
	}

	if (FuncName=="AccountCompany") {
		string retAccountCompany;
	
		retAccountCompany=AccountCompany();
		ret="RET:"+retAccountCompany;
	}

	if (FuncName=="AccountCurrency") {
		string retAccountCurrency;
	
		retAccountCurrency=AccountCurrency();
		ret="RET:"+retAccountCurrency;
	}

	if (FuncName=="MathLog") {
		double retMathLog;
		double x;
	
		index=0;
		x= NStrToDouble(Args[index]);
		index++;
	
		retMathLog=MathLog(x);
		ret="RET:"+retMathLog;
	}

	if (FuncName=="MarketInfo") {
		double retMarketInfo;
		int type;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		type= StrToInteger(Args[index]);
		index++;
	
		retMarketInfo=MarketInfo(symbol, type);
		ret="RET:"+retMarketInfo;
	}

	if (FuncName=="iBars") {
		int retiBars;
		int timeframe;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
	
		retiBars=iBars(symbol, timeframe);
		ret="RET:"+retiBars;
	}

	if (FuncName=="iOpen") {
		double retiOpen;
		int shift;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiOpen=iOpen(symbol, timeframe, shift);
		ret="RET:"+retiOpen;
	}

	if (FuncName=="iClose") {
		double retiClose;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiClose=iClose(symbol, timeframe, shift);
		ret="RET:"+retiClose;
	}

	if (FuncName=="iHigh") {
		double retiHigh;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiHigh=iHigh(symbol, timeframe, shift);
		ret="RET:"+retiHigh;
	}

	if (FuncName=="iLow") {
		double retiLow;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiLow=iLow(symbol, timeframe, shift);
		ret="RET:"+retiLow;
	}

	if (FuncName=="iTime") {
		datetime retiTime;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiTime=iTime(symbol, timeframe, shift);
		ret="RET:"+retiTime;
	}

	if (FuncName=="iVolume") {
		double retiVolume;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		shift= StrToInteger(Args[index]);
		index++;
	
		retiVolume=iVolume(symbol, timeframe, shift);
		ret="RET:"+retiVolume;
	}

	if (FuncName=="iBarShift") {
		int retiBarShift;
		datetime time;
		bool exact=false;
	
		index=0;
		symbol= ""+(Args[index]);
		index++;
		timeframe= StrToInteger(Args[index]);
		index++;
		time= NStrToDouble(Args[index]);
		index++;
		exact= StrToInteger(Args[index]);
		index++;
	
		retiBarShift=iBarShift(symbol, timeframe, time, exact);
		ret="RET:"+retiBarShift;
	}

	if (FuncName=="OrdersTotal") {
		int retOrdersTotal;
	
		retOrdersTotal=OrdersTotal();
		ret="RET:"+retOrdersTotal;
	}

	if (FuncName=="OrderLots") {
		double retOrderLots;
	
		retOrderLots=OrderLots();
		ret="RET:"+retOrderLots;
	}

	if (FuncName=="OrderSelect") {
		bool retOrderSelect;
		int index;
		int select;
	
		index=0;
		index= StrToInteger(Args[index]);
		index++;
		select= StrToInteger(Args[index]);
		index++;
	
		retOrderSelect=OrderSelect(index, select);
		ret="RET:"+retOrderSelect;
	}

	if (FuncName=="GetLastError") {
		int retGetLastError;
	
		retGetLastError=GetLastError();
		ret="RET:"+retGetLastError;
	}

	if (FuncName=="HistoryTotal") {
		int retHistoryTotal;
	
		retHistoryTotal=HistoryTotal();
		ret="RET:"+retHistoryTotal;
	}

	if (FuncName=="OrderCommission") {
		double retOrderCommission;
	
		retOrderCommission=OrderCommission();
		ret="RET:"+retOrderCommission;
	}

	if (FuncName=="OrderExpiration") {
		datetime retOrderExpiration;
	
		retOrderExpiration=OrderExpiration();
		ret="RET:"+retOrderExpiration;
	}

	if (FuncName=="OrderMagicNumber") {
		int retOrderMagicNumber;
	
		retOrderMagicNumber=OrderMagicNumber();
		ret="RET:"+retOrderMagicNumber;
	}

	if (FuncName=="OrderOpenPrice") {
		double retOrderOpenPrice;
	
		retOrderOpenPrice=OrderOpenPrice();
		ret="RET:"+retOrderOpenPrice;
	}

	if (FuncName=="OrderProfit") {
		double retOrderProfit;
	
		retOrderProfit=OrderProfit();
		ret="RET:"+retOrderProfit;
	}

	if (FuncName=="OrderStopLoss") {
		double retOrderStopLoss;
	
		retOrderStopLoss=OrderStopLoss();
		ret="RET:"+retOrderStopLoss;
	}

	if (FuncName=="OrderSwap") {
		double retOrderSwap;
	
		retOrderSwap=OrderSwap();
		ret="RET:"+retOrderSwap;
	}

	if (FuncName=="OrderTakeProfit") {
		double retOrderTakeProfit;
	
		retOrderTakeProfit=OrderTakeProfit();
		ret="RET:"+retOrderTakeProfit;
	}

	if (FuncName=="OrderType") {
		int retOrderType;
	
		retOrderType=OrderType();
		ret="RET:"+retOrderType;
	}

	if (FuncName=="OrderTicket") {
		int retOrderTicket;
	
		retOrderTicket=OrderTicket();
		ret="RET:"+retOrderTicket;
	}

	if (FuncName=="OrderSymbol") {
		string retOrderSymbol;
	
		retOrderSymbol=OrderSymbol();
		ret="RET:"+retOrderSymbol;
	}

	if (FuncName=="IsConnected") {
		bool retIsConnected;
	
		retIsConnected=IsConnected();
		ret="RET:"+retIsConnected;
	}

	if (FuncName=="IsDemo") {
		bool retIsDemo;
	
		retIsDemo=IsDemo();
		ret="RET:"+retIsDemo;
	}

	if (FuncName=="IsDllsAllowed") {
		bool retIsDllsAllowed;
	
		retIsDllsAllowed=IsDllsAllowed();
		ret="RET:"+retIsDllsAllowed;
	}

	if (FuncName=="IsLibrariesAllowed") {
		bool retIsLibrariesAllowed;
	
		retIsLibrariesAllowed=IsLibrariesAllowed();
		ret="RET:"+retIsLibrariesAllowed;
	}

	if (FuncName=="IsStopped") {
		bool retIsStopped;
	
		retIsStopped=IsStopped();
		ret="RET:"+retIsStopped;
	}

	if (FuncName=="IsTesting") {
		bool retIsTesting;
	
		retIsTesting=IsTesting();
		ret="RET:"+retIsTesting;
	}

	if (FuncName=="IsTradeAllowed") {
		bool retIsTradeAllowed;
	
		retIsTradeAllowed=IsTradeAllowed();
		ret="RET:"+retIsTradeAllowed;
	}

	if (FuncName=="RefreshRates") {
		bool retRefreshRates;
	
		retRefreshRates=RefreshRates();
		ret="RET:"+retRefreshRates;
	}

	if (FuncName=="HaveTicks") {
		bool retHaveTicks;
	
		retHaveTicks=HaveTicks();
		ret="RET:"+retHaveTicks;
	}

	if (FuncName=="ActsPerTick") {
		int retActsPerTick;
		int val;
	
		index=0;
		val= StrToInteger(Args[index]);
		index++;
	
		retActsPerTick=ActsPerTick(val);
		ret="RET:"+retActsPerTick;
	}

	if (FuncName=="OrderCloseTime") {
		datetime retOrderCloseTime;
	
		retOrderCloseTime=OrderCloseTime();
		ret="RET:"+retOrderCloseTime;
	}

        Log(ret+" "+MGetLastError());        
	return (ret);
}
        
