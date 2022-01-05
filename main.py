#!/usr/bin/env python3
import os
import multiprocessing as mp
import sysv_ipc
import random
key = 135
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)
keyP = 200
mqP =sysv_ipc.MessageQueue(keyP, sysv_ipc.IPC_CREAT)

class Card:
	def __init__(self,name):
		self.name=name

class Joueur:
	def __init__(self, n,c): # n numero et c cartes en main
		self.n=n
		self.c=c
		self.pts=0
	def addC (self,carte): # On peut ajouter une carte à sa main
		self.c.append(carte)
	def print(self): # Fonction print
		print("Joueur", self.numero)	
	def checkWin(self): # Checker s"il peut gagner la partie
		return len(set(self.c))==1
	def addPts(self):
		if self.c[0]=="Feet":
			self.pts=self.pts+1
			return 1
		if self.c[0]=="Bike":
			self.pts=self.pts+2
			return 2
		if self.c[0]=="Train":
			self.pts=self.pts+4
			return 4	
		if self.c[0]=="Car":
			self.pts=self.pts+3
			return 3
		if self.c[0]=="Airplane":
			self.pts=self.pts+5
			return 5	

class Offre:
	def __init__(self, player, nb):   # Statut de l'offre, joueur qui propose et recoit, cartes mises dans l'offre
		self.stateOfOffer="noOffer"
		self.playerO=player
		self.nbCards	= nb	


def game(listOffer,sG,listPlayer):
  while (gameState):
    for _ in range(nbPlayer):	
      sG().wait			
    for i in range(len(listOffer)):
      del listOffer[i]
    for i in range(0,4):
      if(listPlayer[i].checkWin()):
        print("Le joueur "+listPlayer[i].str(n)+" a déclaré avoir fini avec cette main :"+listPlayer[i].c+" il a engrengé "+listPlayer[i].addPts()+" points")
        if listPlayer[i].pts>= limpts:
          gameState=False
       
def player(pack,listOffer,s,sG,lock,np):
  global hand
  for i in range(5):
    with lock:
      listPlayer[np].c.append(pack.pop()) #On tire une carte
  while(gameState):
    mqP.send("Hand of player "+ str(np+1) +": ",listPlayer[np].c)
    offre=int(input("Want to make an offer ? \nPut a nbr btw 1 and "+str(nbPlayer)+ " \nIf not, put another number")) 
    with lock:
      if 0<offre<4:
        PlayerOffer=input("Which card?")
        listOffer.append(offre)
      else:
        listOffer.append(0)
    for i in range(nbPlayer):
      if	((np+i)%nbPlayer!=np):
        s[(np+i)%nbPlayer].signal()
    for i in range(nbPlayer-1):
      print("Waiting of "+nbPlayer-1-i+ " others")
      s[np].wait
      server = mp.Thread(target=server, args=(listOffer[np],hand,np,PlayerOffer),)
      client = mp.Thread(target=client, args =(listOffer,hand,lock))
      server.start()
      client.start()
      server.join()
      client.join()
      sG.signal()

def server(offer,np,PlayerOffer):
  global hand
  global offre
  while True:
    m, type=mq.receive()
    if t==0:
      mq.remove()
      break
    if t==np:
      offer.stateOfOffer="agreed"
      u=m.decode()
      u=u.split()
      ProcessVisé=u[0]
      RecievdCard=u[1]
      for i in range(offer.nbCards):
        hand.append(RecievdCard)
      mq.send(PlayerOffer, type=ProcessVisé)
      k=0
      for i in range (len(hand)):
        if hand[i]==PlayerOffer:
          del hand[i]
          k+=1
          if k==offer.nbCards:
            break
            
            
def client(listOffer,lock):
  global hand
  print("List of offers :", offers)
  offre=int(input("Interested? Write the number of offer to accept, or 0 to refuse all"))
  if 0<offre<(len(listOffer)+1):
    offre=offre-1
    with lock:
      if(listOffer[offre]!="agreed"):
        carte=echangeC()
        msg=carte+" "+os.getpid()
        msg = msg.encode()
        mq.send(msg,offre[offre].joueurSource)
        m,t=mq.receive()
        if t==os.getpid():
          msg=m.decode()
          for i in range(listOffer[offre].nbCards -1):
            hand2.append(msg)
        j=0
        for i in range (len(hand)-1):
          if hand[i]==carte:
            del hand[i]
          j+=1
          if j==listOffer[offre].nbCards:
            break
          for i in range(len(listOffer) -1):
            quit=""
            quit=quit.encode()
            mq.send(quit,i)
        else:
          print("Sorry, the offer was already accepted")
'''
def instancieListJoueur(nbPlayer): #ToC
  l=[]
  for i in range(nbPlayer):
    l.append(str(input("Entrer le nom du joueur "+ str( i)+" : ")))
  return l
'''
if __name__ == "__main__":
	with mp.Manager() as manager:
		listPlayer=[]
		while True:
			print("Number of players connected: "+str(len(listPlayer)))
			m,t=mqP.receive()
			if t==5:
				mDecoded=m.decode()
				listPlayer.append(Joueur(int(mDecoded),[]))
			if len(listPlayer)>3:
				print("All players connected! We launch the game :)")
				break
		gameState=True
		s=[]
		sG=[]
		offers=[]
		nbPlayer=4
		for i in range(len(listPlayer)):
			s.append(0)
		lock=mp.Lock()
		# On ajoute les carCartetes à la pioche	
		pack = manager.list()
		listOffer=[]
		for i in range(5):
			pack.append("Car") #On enleve 1 moyen, car autant de moyen que de joueur
			pack.append("Train")
			pack.append("Airplane")
			pack.append("Bike")
			pack.append("Feet")
		random.shuffle(pack)
		players=[0,0,0,0]
		for i in range(nbPlayer):
		  players[i] = mp.Process(target=player, args=(pack,listOffer,s,sG,lock,i))
		game = mp.Process(target=game, args =(listOffer,lock,pack,listPlayer,sG))
		game.start()
		for k in players:
			k.start()
		game.join()
		for u in players:
			u.join()