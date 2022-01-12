import sysv_ipc
from multiprocessing import Manager
import threading
import random

key= 200
keyGame=300
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
mqGame = sysv_ipc.MessageQueue(keyGame, sysv_ipc.IPC_CREAT)
playing = True
bell_lock = threading.Lock()

def deck():
    deck = []
    transports = ["Feet","Bike", "Train", "Car", "Airplane"]
    for j in transports[:n] : #n moyen de transport pour n joueurs
        for _ in range(5):
            deck.append(j)
    random.shuffle(deck)
    return deck

def bell(pid):
    bell_lock.acquire() #lock mutext
    gagner = False
    list = hand[pid]
    if list.count(list[0]) == len(list):
        gagner = True
    bell_lock.release()#release mutex
    return gagner

#will be called at every update of the dicti
def offer_display():
    mes = str(offers).encode()
    mqGame.send(mes, type=3)

def make_offer():
    pass

def accept_offer():
    pass

def jouer(pid):
    mes = "Votre main est: "+str(hand[pid])
    mes = mes.encode()
    mq.send(mes, type=pid)
    while playing:
        mes = "What do yo want to do? Make an offer(F) or accept an offer(A), else wait!"
        mes=mes.encode()
        mq.send(mes, type=pid)
        m,_= mq.receive(type=pid+10000)


def connection(n):
    joueurs = 0
    cartes = deck()
    print(cartes)
    listpid=[]
    k = 0
    while True:
        pid, _ = mq.receive(type=1)
        pid = int(pid.decode())
        if joueurs < n:
            joueurs += 1
            listpid.append(pid)
            offers[pid] = []
            hand[pid] = cartes[k:k+5]
            scores[pid] = 0
            #locks[pid]=threading.Lock()
            available[pid] = True
            mes = "Ton identifiant est: " + str(pid)
            mes = mes.encode()
            mq.send(mes, type=pid)
            play = threading.Thread(target=jouer, args=(pid,))
            play.start()
            print(listpid)
        elif joueurs == n:
            for i in listpid:
              m="le jeu peut commencer "
              m=m.encode()
              mq.send(m,type=i)
            print("Le jeu peut commencer")
            mes = "La partie est pleine"
            mes = mes.encode()
            mq.send(mes, type=pid)
            break
        k += 5


if __name__ == "__main__":
    with Manager() as manager:
        offers = manager.dict()
        hand = manager.dict()
        scores = manager.dict()
        locks = manager.dict()
        available = manager.dict()
        n = int(input("Combien de joueurs dans la partie : "))
        connection(n)
