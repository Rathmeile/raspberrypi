#!/bin/python3

from socket import *

host = "127.0.0.1"

print( host )

port=7777

s=socket(AF_INET, SOCK_STREAM)

print("socket made")

s.connect((host,port))

print("socket connected!!!")

msg=s.recv(1024)

print(f"Message from server : {msg}")

s.send(b'"{"name":"solax1","bpower":"value1"}\r\n')
s.send(b'close\r\n')

s.close
