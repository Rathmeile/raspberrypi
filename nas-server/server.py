#!/bin/python3

from socket import *
import time

TIMEOUT = 5

host = "127.0.0.1"

print(host)

port = 7777

s = socket(AF_INET, SOCK_STREAM)

print("Socket Made")

s.bind((host,port))

print("Socket Bound")

s.listen(5)

print("Listening for connections...")

while True:
  c, addr = s.accept()
  c.send (b'Welcome to this python server\r\n')
  print(f"Connection established to {addr}")
  # data = raw_input("Enter data to be sent: ")
  # cmd.send (data)
  connected = True
  emptyReceives = 0
  while connected:
    rcdData = c.recv(1024).decode()
    if rcdData in ['exit', 'close', 'quit']:
      connected = False
    if rcdData == '':
      emptyReceives = emptyReceives + 1
    else:
      print(f"Data received: {rcdData}")
    if emptyReceives > TIMEOUT:
      connected = False
      print("Connection lost")
    if not connected:
      time.sleep(1)
  c.close()

