from multiprocessing.managers import BaseManager as MyManager
import os
import sys
import random
import sysv_ipc
import signalt
import time
import ascii_art


key = 300
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
MyManager.register('sm')
m = MyManager(address=("127.255.255.255", 20), authkey=b'abracadabra')
m.connect()
sm = m.sm()
hands_items = {}
deck=[]

def deck(): #Designating and Shuffling cards in deck
    global deck #deck() function has now acces to theglobal variable [String]deck
    deck = []
    transports = ["Feet", "Bike", "Train", "Car", "Airplane"]
    for j in transports[:n]: #:n => for n different cards if there is n player
        for _ in range(5):
            deck.append(j)
    random.shuffle(deck)
    return deck

def game():
    global deck
    global hands_items
    n = int(input("Number n of players:"))
    deck = deck(n)
    hands_items = {}
    i, k = 0, 0
    while i < n: 
        pid, _ = mq.receive(type=1)
        pid = int(pid.decode())
        offers = sm.get_offers() #Disctionnary type
        offers_items=[]
        sm.set_offers(offers_items, pid) #{pid: []}
        sm.set_flag(True, pid)
        main = deck[k:k + 5]
        hands_items[pid] = main
        art=ascii_art.title()
        toSend = art+"\nWelcome Player "+str(pid)+"! \n You already know the rules, so no need to explain them again :p \n You're now waiting for your friends, at least if you have them."
        toSend = toSend.encode()
        #Sending the pid of the server to each client so they have it they may need it to ring the bell
        mq.send(toSend, type=pid)
        pid_server=str(os.getpid()) # will send its owns pid (ppid variable in client file)
        pid_server=pid_server.encode()
        mq.send(pid_server, type=pid)
        i,k=i+1,k+5
    for pid, list in hands_items.items():
        hand_pid = (' '.join(map(str, list))).encode() #send the initial hand for each client
        mq.send(hand_pid, type=pid)
    signal.signal(signal.SIGUSR2, handler) #ToC SIGNAL USED
    signal.pause() #panse and wait for a signal

#End signal handler (SIGUSR2)
def handler(sig, frame):
    if sig == signal.SIGUS24:
        for pid in hands_items.keys():
            os.kill(pid, signal.SIGUSR2) #send SIGUSR2 to process's pid
    print("THE GAME IS OOOOVER!") #Change print to mq.send
    print("Recovering Scores Table")
    waitingStyle()
    print(sm.get_points())
    While True:
        kp=input("Do you want to keep going? Put yes to play :) or anything to quit :(")
        if kp =="yes":
            waitingStyle()
            print("Welcome again!")
            game()
            break
        else:
            print(ascii_art.credits())
            print("See you soon!")
            mq.remove() #Quiting and removing the message queue
            quit()

#Stylistic waiting
def waitingStyle():
    print("",end="")
    time.sleep(1) #do some work here...
    print("\r.  ",end="")
    time.sleep(1) #do some more work here...
    print("\r.. ",end="")
    time.sleep(1) #do even more work...
    print("\r...",end="")
    time.sleep(1) #gratuitious amounts of work...

if __name__ == "__main__":
    pts=sm.get_points()
    for pid in hands_items.keys():
        sm.set_points(0,pid)
    game()