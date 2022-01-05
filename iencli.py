#!/usr/bin/env python3
import os
import sysv_ipc

key = 200

try:
    mq = sysv_ipc.MessageQueue(key)
except sysv_ipc.ExistentialError:
    print("Cannot connect to message queue", key, ", terminating.")
    sys.exit(1)
while True:
  t=input("Voulez vous jouer ? oui/non")
  if t=="oui":
    break()
mq.send(os.pid(),type=5)
while True:
  m,t=mq.receive(type=(os.pid()))
	print(m)