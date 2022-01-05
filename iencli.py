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
  t=input("Voulez vous jouer ? oui/non  ")
  if t=="oui":
    break
pid=os.getpid()
m=str(pid).encode()
mq.send(m,type=5)
state = True
while True:
	if state:
		m,t=mq.receive(type=(os.getpid()))
		m=m.decode()
		if m == "done":
			state = False
		else :
			print(m)
	else :
		toSend=input("\n")
		msg=toSend.encode()
		mq.send(msg,type=5)
		state=False