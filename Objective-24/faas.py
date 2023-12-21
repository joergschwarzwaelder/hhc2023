import websocket
import _thread
import time
import rel
import json
import urllib.request
import re
import getpass

missingfish={}
myuser=-1

################
## Fishing WS ##
################
def phish_on_open(ws):
  print("Gotta Catch 'Em All 🎣")
  ws.send('cast')

def phish_on_close(ws, close_status_code, close_msg):
  print("** closed Phish connection:"+str(close_msg))
def phish_on_error(ws,error):
  print("** error in Phish connection:"+str(error))

##
## message from fishing WS
##
def phish_on_message(ws,message):
  global missingfish

## fresh fish caught
  if message[0:2]=='f:':
    y=json.loads(message[2:])
    if 'fish' in y  and  'name' in y['fish']:
      del missingfish[y['fish']['name']]
      print(f"{time.ctime()}: *** caught 🐠 {y['fish']['name']}, {len(missingfish)} more to go")
      if(len(missingfish)==0):
        exit()
      ws.send('cast')

## fish inventory
  if message[0:2]=='i:':
    y=json.loads(message[2:])
    if 'fishCaught' in y:
      for v in y['fishCaught']:
        del missingfish[v['name']]
      print(f"{len(missingfish)} 🐠 missing...")
      if(len(missingfish)==0):
        exit()
      for fish in missingfish:
        print(f"🐠 missing: {fish}")
      print(f"{len(missingfish)} 🐠 missing...")

## process fish on the line event
  if message[0:2]=='e:':
    y=json.loads(message[2:])
    if myuser in y and 'onTheLine' in y[myuser] and y[myuser]['onTheLine'] and y[myuser]['onTheLine'] in missingfish:
        ws.send('reel')

################
## HHC2023 WS ##
################
def on_message(ws, message):
  global myuser
  y=json.loads(message)
  if y['type'] == 'WS_USERS' and y['initialLogin']:
    for k in y['users']:
      myuser=k
    ws.send('{ "type": "setSail" }')
    return
  if y['type'] == 'SET_SAIL':
    print("Dockslip "+y['dockSlip'])
    phish_ws=websocket.WebSocketApp('wss://2023.holidayhackchallenge.com/sail?dockSlip='+y['dockSlip'],
                            on_open=phish_on_open,
                            on_message=phish_on_message,
                            on_error=phish_on_error,
                            on_close=phish_on_close)
    phish_ws.run_forever(origin='https://2023.holidayhackchallenge.com',host='2023.holidayhackchallenge.com',dispatcher=rel, reconnect=5)
    rel.signal(2, rel.abort)
    rel.dispatch()
    return
  if y['type'] == 'DENNIS_NEDRY':
    print(y['messages'][0])
    trylogin()


def on_error(ws, error):
  return

def on_close(ws, close_status_code, close_msg):
  print("### closed ###")

def on_open(ws):
  ws.send('{ "type": "WS_CONNECTED", "session": null, "protocol": "43ae08fd-9cf2-4f54-a6a6-8454aef59581" }')
  trylogin()

def trylogin():
  user=input("HHC2023 🪿  username:")
  passw=getpass.getpass("HHC2023 🪿  password:")
  ws.send(json.dumps({"type":"WS_LOGIN","usernameOrEmail":user,"password":passw}))

if __name__ == "__main__":

## load names of all fish species from fish density reference
  rex=re.compile(r'.*>(.*)<',re.S)
  with urllib.request.urlopen('https://2023.holidayhackchallenge.com/sea/fishdensityref.html') as response:
    html=response.read().decode('utf-8').split("\n")
    allfish=[ rex.match(i).groups()[0] for i in html if "h3" in i]
    for f in allfish:
      missingfish[f]=1

## create HHC2023 WS
  ws = websocket.WebSocketApp('wss://2023.holidayhackchallenge.com/ws',
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)

  ws.run_forever(origin='https://2023.holidayhackchallenge.com',host='2023.holidayhackchallenge.com',dispatcher=rel, reconnect=5)
  rel.signal(2, rel.abort)
  rel.dispatch()
