
class cMarketInfo:
    MODE_LOW  = 1#Low day price.#
    MODE_HIGH = 2#High day price.#
    MODE_TIME = 5#The last incoming tick time (last known server time).#
    MODE_BID  = 9#Last incoming bid price. For the current symbol, it is stored in the predefined variable Bid#
    MODE_ASK  = 10#Last incoming ask price. For the current symbol, it is stored in the predefined variable Ask#
    MODE_POINT= 11#Point size in the quote currency. For the current symbol, it is stored in the predefined variable Point" 
    MODE_DIGITS = 12# Count of digits after decimal point in the symbol prices. For the current symbol, it is stored in the predefined variable Digits#
    MODE_SPREAD  = 13# Spread value in points.#
    MODE_STOPLEVEL=  14#Stop level in points.#
    MODE_LOTSIZE  = 15#Lot size in the base currency.#
    MODE_TICKVALUE= 16#Tick value in the deposit currency.#
    MODE_TICKSIZE  = 17#Tick size in the quote currency.#

    MODE_SWAPLONG=18 #Swap of the long position. 
    MODE_SWAPSHORT=19 #Swap of the short position. 
    MODE_STARTING=20 #Market starting date (usually used for futures). 
    MODE_EXPIRATION=21 #Market expiration date (usually used for futures). 
    MODE_TRADEALLOWED=22 #Trade is allowed for the symbol. 
    MODE_MINLOT=23 #Minimum permitted amount of a lot. 
    MODE_LOTSTEP=24 #Step for changing lots. 
    MODE_MAXLOT=25 #Maximum permitted amount of a lot. 
    MODE_SWAPTYPE=26 #Swap calculation method. 0 - in points; 1 - in the symbol base currency; 2 - by interest; 3 - in the margin currency. 
    MODE_PROFITCALCMODE=27 #Profit calculation mode. 0 - Forex; 1 - CFD; 2 - Futures. 
    MODE_MARGINCALCMODE=28 #Margin calculation mode. 0 - Forex; 1 - CFD; 2 - Futures; 3 - CFD for indices. 
    MODE_MARGININIT=29 #Initial margin requirements for 1 lot. 
    MODE_MARGINMAINTENANCE=30 #Margin to maintain open positions calculated for 1 lot. 
    MODE_MARGINHEDGED=31 #Hedged margin calculated for 1 lot. 
    MODE_MARGINREQUIRED=32 #Free margin required to open 1 lot for buying. 
    MODE_FREEZELEVEL=33 #Order freeze level in points. If the execution price lies within the range defined by the freeze level, the order cannot be modified, cancelled or closed. 



class cOrderSend:
    OP_BUY=0 #Buying position. 
    OP_SELL=1 #Selling position. 
    OP_BUYLIMIT= 2 #Buy limit pending position. 
    OP_SELLLIMIT= 3 #Sell limit pending position. 
    OP_BUYSTOP= 4 #Buy stop pending position. 
    OP_SELLSTOP= 5 #Sell stop pending position. 

class cOrderSelect:
    SELECT_BY_POS    = 0
    SELECT_BY_TICKET = 1

class cGetLastError:
    ERR_NO_ERROR =0 #No error returned. 
    ERR_NO_RESULT=1 #No error returned, but the result is unknown. 
    ERR_COMMON_ERROR=2 #Common error. 
    ERR_INVALID_TRADE_PARAMETERS=3# Invalid trade parameters. 
    ERR_SERVER_BUSY=4 #Trade server is busy. 
    ERR_OLD_VERSION=5 #Old version of the client terminal. 
    ERR_NO_CONNECTION=6 #No connection with trade server. 
    ERR_NOT_ENOUGH_RIGHTS=7 #Not enough rights. 
    ERR_TOO_FREQUENT_REQUESTS=8 #Too frequent requests. 
    ERR_MALFUNCTIONAL_TRADE=9 #Malfunctional trade operation. 
    ERR_ACCOUNT_DISABLED=64 #Account disabled. 
    ERR_INVALID_ACCOUNT=65 #Invalid account. 
    ERR_TRADE_TIMEOUT=128 #Trade timeout. 
    ERR_INVALID_PRICE=129 #Invalid price. 
    ERR_INVALID_STOPS=130 #Invalid stops. 
    ERR_INVALID_TRADE_VOLUME=131 #Invalid trade volume. 
    ERR_MARKET_CLOSED=132 #Market is closed. 
    ERR_TRADE_DISABLED=133 #Trade is disabled. 
    ERR_NOT_ENOUGH_MONEY=134 #Not enough money. 
    ERR_PRICE_CHANGED=135 #Price changed. 
    ERR_OFF_QUOTES=136 #Off quotes. 
    ERR_BROKER_BUSY=137 #Broker is busy. 
    ERR_REQUOTE=138 #Requote. 
    ERR_ORDER_LOCKED=139 #Order is locked. 
    ERR_LONG_POSITIONS_ONLY_ALLOWED=140 #Long positions only allowed. 
    ERR_TOO_MANY_REQUESTS=141 #Too many requests. 
    ERR_TRADE_MODIFY_DENIED=145 #Modification denied because order too close to market. 
    ERR_TRADE_CONTEXT_BUSY=146 #Trade context is busy. 
    ERR_TRADE_EXPIRATION_DENIED=147 #Expirations are denied by broker. 
    ERR_TRADE_TOO_MANY_ORDERS=148 #The amount of open and pending orders has reached the limit set by the broker. 
    ERR_TRADE_HEDGE_PROHIBITED=149 #An attempt to open a position opposite to the existing one when hedging is disabled. 
    ERR_TRADE_PROHIBITED_BY_FIFO=150 #An attempt to close a position contravening the FIFO rule. 

    ERR_NO_MQLERROR=4000 #No error. 
    ERR_WRONG_FUNCTION_POINTER=4001 #Wrong function pointer. 
    ERR_ARRAY_INDEX_OUT_OF_RANGE=4002 #Array index is out of range. 
    ERR_NO_MEMORY_FOR_CALL_STACK=4003 #No memory for function call stack. 
    ERR_RECURSIVE_STACK_OVERFLOW=4004 #Recursive stack overflow. 
    ERR_NOT_ENOUGH_STACK_FOR_PARAM=4005 #Not enough stack for parameter. 
    ERR_NO_MEMORY_FOR_PARAM_STRING=4006 #No memory for parameter string. 
    ERR_NO_MEMORY_FOR_TEMP_STRING=4007 #No memory for temp string. 
    ERR_NOT_INITIALIZED_STRING=4008 #Not initialized string. 
    ERR_NOT_INITIALIZED_ARRAYSTRING=4009 #Not initialized string in array. 
    ERR_NO_MEMORY_FOR_ARRAYSTRING=4010 #No memory for array string. 
    ERR_TOO_LONG_STRING=4011 #Too long string. 
    ERR_REMAINDER_FROM_ZERO_DIVIDE=4012 #Remainder from zero divide. 
    ERR_ZERO_DIVIDE=4013 #Zero divide. 
    ERR_UNKNOWN_COMMAND=4014 #Unknown command. 
    ERR_WRONG_JUMP=4015 #Wrong jump (never generated error). 
    ERR_NOT_INITIALIZED_ARRAY=4016 #Not initialized array. 
    ERR_DLL_CALLS_NOT_ALLOWED=4017 #DLL calls are not allowed. 
    ERR_CANNOT_LOAD_LIBRARY=4018 #Cannot load library. 
    ERR_CANNOT_CALL_FUNCTION=4019 #Cannot call function. 
    ERR_EXTERNAL_CALLS_NOT_ALLOWED=4020 #Expert function calls are not allowed. 
    ERR_NO_MEMORY_FOR_RETURNED_STR=4021 #Not enough memory for temp string returned from function. 
    ERR_SYSTEM_BUSY=4022 #System is busy (never generated error). 
    ERR_INVALID_FUNCTION_PARAMSCNT=4050 #Invalid function parameters count. 
    ERR_INVALID_FUNCTION_PARAMVALUE=4051 #Invalid function parameter value. 
    ERR_STRING_FUNCTION_INTERNAL=4052 #String function internal error. 
    ERR_SOME_ARRAY_ERROR=4053 #Some array error. 
    ERR_INCORRECT_SERIESARRAY_USING=4054 #Incorrect series array using. 
    ERR_CUSTOM_INDICATOR_ERROR=4055 #Custom indicator error. 
    ERR_INCOMPATIBLE_ARRAYS=4056 #Arrays are incompatible. 
    ERR_GLOBAL_VARIABLES_PROCESSING=4057 #Global variables processing error. 
    ERR_GLOBAL_VARIABLE_NOT_FOUND=4058 #Global variable not found. 
    ERR_FUNC_NOT_ALLOWED_IN_TESTING=4059 #Function is not allowed in testing mode. 
    ERR_FUNCTION_NOT_CONFIRMED=4060 #Function is not confirmed. 
    ERR_SEND_MAIL_ERROR=4061 #Send mail error. 
    ERR_STRING_PARAMETER_EXPECTED=4062 #String parameter expected. 
    ERR_INTEGER_PARAMETER_EXPECTED=4063 #Integer parameter expected. 
    ERR_DOUBLE_PARAMETER_EXPECTED=4064 #Double parameter expected. 
    ERR_ARRAY_AS_PARAMETER_EXPECTED=4065 #Array as parameter expected. 
    ERR_HISTORY_WILL_UPDATED=4066 #Requested history data in updating state. 
    ERR_TRADE_ERROR=4067 #Some error in trading function. 
    ERR_END_OF_FILE=4099 #End of file. 
    ERR_SOME_FILE_ERROR=4100 #Some file error. 
    ERR_WRONG_FILE_NAME=4101 #Wrong file name. 
    ERR_TOO_MANY_OPENED_FILES=4102 #Too many opened files. 
    ERR_CANNOT_OPEN_FILE=4103 #Cannot open file. 
    ERR_INCOMPATIBLE_FILEACCESS=4104 #Incompatible access to a file. 
    ERR_NO_ORDER_SELECTED=4105 #No order selected. 
    ERR_UNKNOWN_SYMBOL=4106 #Unknown symbol. 
    ERR_INVALID_PRICE_PARAM=4107 #Invalid price. 
    ERR_INVALID_TICKET=4108 #Invalid ticket. 
    ERR_TRADE_NOT_ALLOWED=4109 #Trade is not allowed. Enable checkbox "Allow live trading" in the expert properties. 
    ERR_LONGS_NOT_ALLOWED=4110 #Longs are not allowed. Check the expert properties. 
    ERR_SHORTS_NOT_ALLOWED=4111 #Shorts are not allowed. Check the expert properties. 
    ERR_OBJECT_ALREADY_EXISTS=4200 #Object exists already. 
    ERR_UNKNOWN_OBJECT_PROPERTY=4201 #Unknown object property. 
    ERR_OBJECT_DOES_NOT_EXIST=4202 #Object does not exist. 
    ERR_UNKNOWN_OBJECT_TYPE=4203 #Unknown object type. 
    ERR_NO_OBJECT_NAME=4204 #No object name. 
    ERR_OBJECT_COORDINATES_ERROR=4205 #Object coordinates error. 
    ERR_NO_SPECIFIED_SUBWINDOW=4206 #No specified subwindow. 
    ERR_SOME_OBJECT_ERROR=4207 #Some error in object function. 
