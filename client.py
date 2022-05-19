from pickle import OBJ
import socket
from datetime import datetime 
import json

IP =  "192.168.1.191"
PORT = 8000
HEADER = 1024
header={
  "to":IP,
  "from":IP,
  "lenght":0,
  "timestamp":0
}

client = socket.socket()
client.connect((IP, PORT))
print(f"[CONNECTED] Conectado al servidor en {IP}")

while True:
  
  msg = input("Ingrese un mensaje: ")
  header["length"]=len(msg)
  header["timestamp"]=str(datetime.now())
  obj=json.dumps(header)
  client.send(str(obj).encode("utf-8"))
  client.send(msg.encode("utf-8"))
