import SocketServer
import string
import threading, Queue
import time
import socket
import fcntl
import struct
import sys


"""
   ************************************************************
                       Utility Functions
   ************************************************************
"""

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def cleanData(d):
    nd=filter(lambda x:x in string.printable,d)
    return nd
def PurgeQ(Q):
    while not Q.empty():
        oldmsg=Q.get()
        if ApiAdapter.debug: print "Discarding %s"%oldmsg
        Q.task_done()

def WaitHandler():
    while MQL4TCPHandler.instance==None or PH.TP<len(PH.Table)-1:
        print "Handshake not finished" 
        #use import logging for logs. rewrite if needed.
        time.sleep(1)

"""
   ************************************************************
                       Server class. 
   ************************************************************
"""

class MQL4TCPHandler(SocketServer.BaseRequestHandler):
    instance=None
    def handle(self):
        while not ApiAdapter.Stop:
            MQL4TCPHandler.instance=self
            self.data = self.request.recv(1024).strip()#,socket.MSG_DONTWAIT).strip()
            self.data=cleanData(self.data)
            if self.data=='KIL:':break
            if self.data[:4]=='ALM:':PH.TP=2
            Response=ProcessMessage(self.data)
            if ApiAdapter.debug:
                print "Request:",self.data,"Will respond:",Response
            if Response!="":
                self.request.send(Response)
            Response=""
            ApiAdapter.OutQ.put(self.data)
            self.data=""

    
"""
   ************************************************************
                       Main "singleton" class. 
                       2 threads: server and api adapter.
                       2 queues: one for PyAPI posting to server,
                       one for Server posting back the answer to PyAPI
                       to mimick synchronuous behavior.
   ************************************************************
"""

class ApiAdapter:
    # Contain threads, queues, 
    # Protocol phases handler

    def ApiRunner():
        print "ApiRunner:"
        while not ApiAdapter.Stop:
            try:
                Msg=ApiAdapter.InQ.get(timeout=20)
                Reply=ForwardToMQL(Msg)
                ApiAdapter.InQ.task_done()
            except Queue.Empty:
                pass
            except:
                print 'Error %s %s %s'% sys.exc_info()
                ApiAdapter.Stop=True


        print "Killing ApiRunner"
    def ServerThread():
        print "ServerLoop"        
        try:
            ApiAdapter.server.serve_forever()
        except:
            ApiAdapter.server.shutdown()
        print "Killing ServerThread"
    
    OutQ    = Queue.Queue()
    InQ     = Queue.Queue()
    ApiThr  = threading.Thread(target=ApiRunner,args=())
    ServThr = threading.Thread(target=ServerThread,args=())
    server  = None
    Stop    = False
    HOST    = None
    PORT    = None
    instance        = None
    Interface       = None
    ProcessMessage  = None
    debug           = True
    ApiLock         = threading.RLock()
    def ForwardToMQL(self,msg):
        ApiAdapter.ApiLock.acquire()
        RetMsg=None
        WaitHandler()
        PurgeQ(ApiAdapter.OutQ)
        ret=MQL4TCPHandler.instance.request.send(msg)##ApiAdapter.OutQ.put(msg)#
        while not ApiAdapter.Stop:
            try:
                RetMsg=ApiAdapter.OutQ.get(timeout=30)
                ApiAdapter.OutQ.task_done()
            except Queue.Empty:
                RetMsg="RET:-1"
            except:
                ApiAdapter.Stop=True
            finally:
                ApiAdapter.ApiLock.release()
            return RetMsg

        return RetMsg

        
    def __init__(self,ifce=None,port=2900):
        ApiAdapter.Interface='lo' if ifce==None else ifce
        ApiAdapter.PORT=port
        ApiAdapter.HOST=get_ip_address(ApiAdapter.Interface)
        ApiAdapter.instance=self
        print "Bound to %s %d"%(ApiAdapter.HOST,ApiAdapter.PORT)

    def startMachine(self):
        ApiAdapter.server = SocketServer.ThreadingTCPServer(
            (ApiAdapter.HOST, ApiAdapter.PORT),
            MQL4TCPHandler
            )
        #ApiAdapter.ApiThr.setDaemon(True)
        #ApiAdapter.ServThr.setDaemon(True)
        ApiAdapter.ApiThr.start()
        ApiAdapter.ServThr.start()
        

def killall():
    ApiAdapter.Stop=True
    ApiAdapter.ApiLock.release()
    ApiAdapter.server.shutdown()

def FillDetail(m,n):
    Ans=""
    if m!=None:Ans+=m+':'
    if n!=None:Ans+=n
    return Ans

#recv,send,send_detail
def ProcessMessage(M):
    Expected      = PH.Table[PH.TP][0]
    AnswerType    = PH.Table[PH.TP][1]        
    AnswerDetail  = None
    Ans=" "
    if len(PH.Table[PH.TP])>2:
        AnswerDetail  = PH.Table[PH.TP][2]
        
    if M[:len(Expected)]==Expected:
        Ans=FillDetail(AnswerType,AnswerDetail)
    if PH.TP<len(PH.Table)-1:
        PH.TP=PH.TP+1
    return Ans

class PH:
    MsgTypes= ['SYM:', 'DAT:', 'ORD:', 'ALM:', 'FUN:', 'RET:',"SYN:"]
    TP=0
    Table=[
        ("SYN","SYN",None),
        ("SYM",None,"ok"),
        ("ALM","FUN","MathLog(2)"),
        ("RET","ACK")
        ]

"""
----------------------------------------------------------------------------
                         Marshalled API Calls:
----------------------------------------------------------------------------
"""
sys.path.append('.')
sys.path.append('../Generated')
from MQLApi import *


"""
--------------------------------------------------------------------------------
           Stress tests for API. Needed, because they will be used hard
-------------------------------------------------------------------------------
"""
sys.path.append('../Generated')
from MQL4Constants import *

def SimpleTests():
    print AccountBalance()
    print AccountCurrency()
    print OrdersTotal()
    
def forceSimpleTests():
    for k in range(10):
        SimpleTests()

def SimplePriceTest():
    print iClose("EURUSD",15,0)
    print iBars("EURUSD",15)
    print iBars("USDCAD",15)
    print iClose("USDCAD",15,0)
    print iTime("EURUSD",15,0)

def LoopSimplePriceTest():
    N=iBars("EURUSD",15)
    for k in xrange(10):
        print k,iClose("EURUSD",15,k)
        

def OrderSimpleTest():
    sym="EURUSD"
    Ask=MarketInfo(sym,cMarketInfo.MODE_ASK)
    minvol=MarketInfo(sym,cMarketInfo.MODE_MINLOT)
    color=int(0xf1f3ff)
    #symbol, cmd, volume, price, slippage, stoploss, takeprofit, comment, magic, expiration, arrow_color);
    SL=0.0
    TP=0.0
    expir=0
    
    ticket=OrderSend(sym,cOrderSend.OP_BUY,minvol,Ask,3,SL,TP,"3rd Test",22334,expir,color)
    if ticket==-1:
        print "Order failed",GetLastError()
        return

    time.sleep(40)

    Ask=MarketInfo(sym,cMarketInfo.MODE_ASK)    
    Point=MarketInfo(sym,cMarketInfo.MODE_POINT)    
    #(ticket, price, stoploss, takeprofit, expiration, arrow_color);
    SL=Ask-25*Point
    TP=Ask+25*Point
    color=color/2
    Done=OrderModify(ticket,Ask,SL,TP,expir,color)
    if not Done:
        print "Order Modify Failed:", GetLastError()

    time.sleep(40)

    Ask=MarketInfo(sym,cMarketInfo.MODE_ASK)        
    #(ticket, lots, price, slippage, Color)
    color=int(0xffaaaa)
    Done=OrderClose(ticket,minvol,Ask,4,color)
    if not Done:
        print "Order Modify Failed:", GetLastError()


def InitServer():
    global A

    iflist=['eth0','wlan1','lo']

    for iff in iflist:
        try:
            A=ApiAdapter(ifce=iff)
            break
        except IOError:
            print "IF:%s Failed"%iff
            continue
    for k in range(10):
        try:
            A.startMachine()
            break
        except:
            print "Bind failed, retry after sleep"
            time.sleep(20)
            continue
    time.sleep(20)
    SimpleTests()
    SimplePriceTest()

if __name__ == "__main__":

    iflist=['eth0','wlan1','lo']

    for iff in iflist:
        try:
            A=ApiAdapter(ifce=iff)
            break
        except IOError:
            print "IF:%s Failed"%iff
            continue
    for k in range(10):
        try:
            A.startMachine()
            break
        except:
            print "Bind failed, retry after sleep"
            time.sleep(20)
            continue
    time.sleep(20)
    SimpleTests()
    SimplePriceTest()
    LoopSimplePriceTest()
    #OrderSimpleTest()
