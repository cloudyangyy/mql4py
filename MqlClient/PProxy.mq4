//+------------------------------------------------------------------+
//|                                                       PProxy.mq4 |
//|                                                      Razvan Coca |
//|                                                                  |
//+------------------------------------------------------------------+
#property copyright "Razvan Coca"
#property link      ""


#import "user32.dll"
bool GetAsyncKeyState(int Key);
#import
#include <winsock.mqh>

#include <stdlib.mqh>
#include <stderror.mqh>

#define BUFFSIZE 256
//--- input parameters
extern int       Port             = 2900;
extern string    protocol         = "TCP";
//extern string    server_addr      =  "192.168.1.244";
extern string    server_addr      =  "192.168.1.158";
//extern string    server_addr      =  "192.168.1.219";
//extern string    server_addr      =  "127.0.0.1";

//If we have no market, we need to make it run in init.
extern bool      ForceRunInInit   = false; 
//If we have market on the other hand, start() will be called at each tick.
extern bool      ForceLoop        = true; 

extern int MaxCallsPerTick        = 100;
int conn_socket=-1;
int ProtoVersion=1;

/*
   Error Conditions. Named.
*/
int SocketInitErr      =-1;
int SendErr            =-2;
int RecvErr            =-3;
int ProtoHandshakeErr  =-4;

extern bool debug=false;
bool getDebug()
{
   return (debug);
}
#include "mqpyapi_customized.mq4"


//+------------------------------------------------------------------+
//| generic utility functions                                        |
//+------------------------------------------------------------------+


 int Log(string str)
{ 
   int retval=0;
   Print(str);
   return (retval);
}
int SendMsg(string s)
{
   int retval=-1;
   int Buffer[BUFFSIZE];
   ArrayInitialize(Buffer,0.0);
   str2struct(Buffer,ArraySize(Buffer)<<18,s+"\n");
   retval = send(conn_socket, Buffer, ArraySize(Buffer)<<2, 0);
   if(retval==SOCKET_ERROR)
   {
      Log("SendMsg Failed:"+WSAGetLastError());
      return (SendErr);
   }
   if (debug)Log("SendMsg: ["+s+"]");
   return (retval);  
}
string RecvMsg()
{
   int Buffer[BUFFSIZE];
   int retval=-1;
   string s="";
   ArrayInitialize(Buffer,0.0);
   retval = recv(conn_socket, Buffer, ArraySize(Buffer)<<2, 0);
   if(retval==SOCKET_ERROR)
   {
      Log("RecvMsg Failed:"+ WSAGetLastError());
      if (conn_socket>0) closesocket(conn_socket);
      conn_socket=0;
      return("RecvErr");
   }
   s=struct2str(Buffer,ArraySize(Buffer)<<18);
   s=StringTrimRight(s);
   if(debug)Log("RecvMsg: ["+s+" len="+StringLen(s)+"]");
   
   return(s);
}

int InitializeGlobals()
{
   conn_socket  = 0;
   ProtoVersion = 1;  
   if (GlobalVariableCheck("PProxy"))
   {
      Print("EA already running");
      return(-1);
   }
   GlobalVariableSet("PProxy",1);
   return(0);
}
int SocketInit()
{
   int retval;
   int socket_type;
   int server[sockaddr_in];
   int hp;
   int addr[1];
   int wsaData[WSADATA];
   string s;
   string msg;
   int counter=0;
   Log("SocketInit");
   socket_type = SOCK_STREAM; 
   ArrayInitialize(wsaData,0.0);
   retval = WSAStartup(0x202, wsaData);
   Log("WSAStartup returns:"+retval);
   if(retval<0) return(retval);
   addr[0] = inet_addr(server_addr); 
   hp = gethostbyaddr(addr[0], 4, AF_INET);
   s="Server addr:"+addr[0]+" hp: "+  hp;
   Log(s);
   if (hp == 0 )
   {
      if (addr[0]!=0)hp=addr[0];
      else
      {
         Log("Client: Cannot resolve address \""+server_addr+"\": Error :"+WSAGetLastError());
         return(-1);
      }
   }
   int2struct(server,sin_addr,addr[0]);
   int2struct(server,sin_family,AF_INET);
   int2struct(server,sin_port,htons(Port));
   Log("Creating Socket");
   conn_socket = socket(AF_INET, socket_type, 0); 
   if (conn_socket <0 )
   {
        Log("Client: Error Opening socket: Error "+ WSAGetLastError());
        //deinit();
        return(-1);
   }
   else
   {
      Log("Client: socket() is OK.");
      retval=0;
   }
   Log("Client: Client connecting to: "+ server_addr);
   while(True)
   {
      retval=connect(conn_socket, server, ArraySize(server)<<2);
      
      if (retval==SOCKET_ERROR)
      {
         Log("connect() API error:"+retval+" "+WSAGetLastError());
         return(-1);
      }
      else
      {
         retval=0;
         break;
      }
  }
  return(retval);
 }
 
 bool HaveTicks()
 {
   bool val=False;
   //Only if we have ticks we will have start() called. 
   //Otherwise we are forced to do that in init()
   
   val=((!ForceRunInInit) && IsTradeAllowed() );
   if (debug)Log("HaveTicks->"+val);
   return(val);
 }
 
//+------------------------------------------------------------------+
//| expert initialization function                                   |
//+------------------------------------------------------------------+
int init()
  {
//----
   int retval=0;
   if(InitializeGlobals()!=0)return(-1);
   int tsleep=500;
   
   Log("Running init()");   
   /*if (!HaveTicks())
   {
      ForceLoop=true;
      ForceRunInInit=true;
      retval=2;

   }
   else
   {
      if (debug)Log("ForceLoop, tick-wise call to start");
      ForceLoop=false;
      retval=0;
   }*/
   if(IsTesting())
   {
      ForceLoop=false;
      ForceRunInInit=false;
   }
 
     if(ForceRunInInit)
     {
         if (debug)Log("ForceLoop, explicit call to start");
         start();
     }

//----
   return(retval);
  }
//+------------------------------------------------------------------+
//| expert deinitialization function                                 |
//+------------------------------------------------------------------+
int deinit()
  {
//----
   Log("Running deinit()");
   SendMsg("KIL:");
   if (conn_socket>0) closesocket(conn_socket);
   conn_socket=0;
   GlobalVariableDel("PProxy");
//----
   return(0);
  }

//+------------------------------------------------------------------+
//| expert start function                                            |
//+------------------------------------------------------------------+
int start()
  {
   int retval;
   int tsleep=500;
//----
  while (retval<0 && !IsStopped())
   {
      if (conn_socket>0)
      {
         Log("Socket looks ok");
         retval=conn_socket;
         break;
      }
      retval=SocketInit();  
      if(debug)Log("SocketInit->"+retval);
      if (retval<0)
      {
         Log("Error initializing socket"+retval+"sleeping before retry");
         if (conn_socket>0) closesocket(conn_socket);
         conn_socket=0;
         Sleep(tsleep);
         retval=SocketInitErr;
      }
      
   }
  retval=ProtocolHandshake();
   if (retval<0)
   {
      retval=ProtoHandshakeErr;
      Log("ProtocolHandshake->"+retval);
      return (retval);
   }
   else
   {
         Log("ProtocolHandshake ok");
   }
   Log("Running start()");
   retval=-1;
   retval=ProtocolRun();
   
//----
   return(0);
  }
//+------------------------------------------------------------------+
//Message Types:
//SYM: symbol
//DAT: data
//ORD: order
//ALM: alarm
//FUN: api call
//SYN: synchronize with server
int ProtocolHandshake()
{
   int retval;
   string s;
   string rmsg="";
   
   Log("ProtocolHandshake");
   MaxCallsPerTick=5000;
   while(!IsStopped())
   {
      int stime=10000;
      retval=SendMsg("SYN:");
      if(retval<0)
      {
         Log("Cannot SYN to server, sleeping:"+stime/1000+" s");
         //Maybe a better dispatch of errors. Maybe we need to reinit socket
         Sleep(stime);
         SocketInit();
         continue;
      }
      rmsg=RecvMsg();
      if(debug)Log("received:"+rmsg);
      if(StringFind(rmsg,"Error")!=-1)continue;
      if(rmsg=="")SocketInit();
      if(StringFind(rmsg,"SYN:")!=-1)break;
      Log("Waiting for SYN,"+stime/1000+" s");
      Sleep(stime);
      
   }
   Print("iClose(\"EURUSD\",15,0)->"+iClose("EURUSD",15,0));
   s="SYM:"+Symbol()+Period()+" ProtoVersion="+ProtoVersion;
   retval=SendMsg(s);
   if(retval<0) return(retval);
   rmsg=RecvMsg();
   if(StringFind(rmsg,"Error")!=-1)
   {
      Log("Server Not Started");
      return (RecvErr);
   }
   {
      retval=SendMsg("ALM:Start");
      Log("Initiating:ALM:Start->"+retval);
   }

   if(rmsg=="RET:ok")
   {
      retval=0;
   }  
   return (retval);
}


int ProtocolRun()
{
   int retval=0;
   string rmsg;
   string smsg;
   string m;
   int callspertick;
   Log("ProtocolRun");   
   Sleep(100);
   //for(int i=0;i<3;i++)
   callspertick=10;
   while(!IsStopped())
   {
      if (conn_socket==0) SocketInit();
      

      rmsg=RecvMsg();
      if(StringLen(rmsg)==0)
      {
         Log("Null message received, exiting...");
         if(!IsTesting())break;
      }
      /*if(StringSubstr(rmsg,0,3)=="ACK")
      {
         smsg=" ";
         SendMsg(smsg);
         if(debug)Log(smsg);

      }*/
      if(StringSubstr(rmsg,0,4)=="SYM:")
      {
         Log("Symbol");
      }
      if (StringSubstr(rmsg,0,4)=="DAT:")
      {
       Log("Data");
      }
      if(StringSubstr(rmsg,0,4)=="ORD:")
      {
         Log("Order");
      }
      if (StringSubstr(rmsg,0,4)=="ALM:")
      {
         Log("Alarm");
      }
      if (StringSubstr(rmsg,0,4)=="FUN:")
      {
      
         m=StringSubstr(rmsg,4);
         if(debug)Log("FunctionCall:"+m);
         smsg=FunCall(m);
         if (debug)Log("->"+smsg);
         SendMsg(smsg);
         if(debug)Log(smsg);
         callspertick=((callspertick+1)%MaxCallsPerTick);         
      }
      if(ForceLoop)Sleep(10);
      else
      {
         
         if(callspertick<=0)
         {
          if(debug)
          Log("Max Calls Per Tick reached, yielding.."+MaxCallsPerTick);
          break;
         }
         else  
            if (debug) Log("Calls remaining:"+(MaxCallsPerTick-callspertick));
      }
   }
   if (IsStopped())Log("Stopping Protocol Handler");
   return (retval);
   
}

