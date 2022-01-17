import sysv_ipc
import sys
import os
import sys
import threading

key = 300
keyG = 400
pid = os.getpid()

try:
    mq = sysv_ipc.MessageQueue(key)
except sysv_ipc.ExistentialError:
    print("The message queue you're trying to connect to doesn't exist.")
    sys.exit(1)

try:
    gameMq = sysv_ipc.MessageQueue(keyG)
except sysv_ipc.ExistentialError:
    print("The message queue you're trying to connect to doesn't exist.")
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

mq.send(str(pid).encode(), type=1)
# To listen to the server's answer
# To see if we are accepted or no
while True:
    m, _ = mq.receive(type=pid)
    m = m.decode()
    if m == "Tu es accepté dans la partie. En attente d'autres joueurs...":
        print(m)
        break
    if m == "You came too late. A game is already running":
        print(m)
        sys.exit(1)