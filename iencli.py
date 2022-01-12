#!/usr/bin/env python3
import os
import sysv_ipc
import sys

key = 200
keyGame=300

try:
    mq = sysv_ipc.MessageQueue(key)
except sysv_ipc.ExistentialError:
    print("Cannot connect to message queue", key, ", terminating.")
    sys.exit(1)

try:
    mqgame = sysv_ipc.MessageQueue(keyGame)
except sysv_ipc.ExistentialError:
    print("Cannot connect to message queue", keyGame, ", terminating.")
    sys.exit(1)


while True:
	t=input("Want to play ? yes/no  ")
	if t=="yes":
    		break
	elif t=="no":
		print("Quitting..")
		quit()
	else:
		print("Bad input! Try again !")
print("caca")
pid=os.getpid()
m=str(pid).encode()
mq.send(m,type=1)
state = True
counter=0
while True:
	if state:
		print("caca")
		m,t=mq.receive(type=pid)
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