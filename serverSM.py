from multiprocessing.managers import BaseManager as MyManager
import os
import sys
import random
import sysv_ipc
import signal

key = 300
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

def deck(): #Designating and Shuffling cards in deck
    deck = []
    transports = ["Shoes", "Bike", "Train", "Car", "Airplane"]
    for j in transports[:n]: #:n => for n different cards if there is n player
        for _ in range(5):
            deck.append(j)
    random.shuffle(deck)
    return deck

#End signal handler (SIGUSR4)
def handler(sig, frame):
    if sig == signal.SIGUSR4:
        for pid in mains_i.keys():
            os.kill(pid, signal.SIGUSR3) #send SIGUSR3 to process's pid
    print("La partie est terminée")
    sys.exit(1)

if __name__ == "__main__":
    MyManager.register('sm')
    m = MyManager(address=("127.255.255.255", 20), authkey=b'abracadabra')
    m.connect()
    sm = m.sm()
    n = int(input("How many players will play: "))
    deck = deck(n)
    mains_i = {}
    i = 0
    k = 0
    while i < n:
        pid, _ = mq.receive(type=1)
        pid = int(pid.decode())

        # Creating our dict of offers and availability which is empty at the beginning
        offres = sm.get_offers()
        offres[pid] = []
        sm.set_offers(offres)

        dispo = sm.get_flag()
        dispo[pid] = True
        sm.set_flag(dispo)

        main = deck[k:k + 5]
        mains_i[pid] = main
        msg = "You're connected. Waiting for other players..."
        msg = msg.encode()
        #Sending the pid of the server to each client so they have it they may need it to ring the bell
        mq.send(msg, type=pid)
        pid_server=str(os.getpid())
        pid_server=pid_server.encode()
        mq.send(pid_server)

        i += 1
        k += 5
    for pid, list in dict.items():
        main = (' '.join(map(str, list))).encode()
        mq.send(main, type=pid)
    signal.signal(signal.SIGUSR4, handler)
    signal.pause()
#Fermer les msgs queues
#Continuer la partie
#Faire dict de scores