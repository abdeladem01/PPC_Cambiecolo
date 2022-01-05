'''
#!/usr/bin/env python3
import sys
import time
import os
import multiprocessing
import threading
from queue import Queue
import sysv_ipc
import concurrent.futures

key = 135
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)

//pour le reste du pseudo code : pack désigne la liste de l'ensemble du jeu de carte

Structure Player :
|	entier n,  listString[] c, entier pts
|	Constructeur Player(entier n app {1 -> 4}, listString[] c):
|	|	this.n  =n; this.c = c ; this.pts = 0;
|	Fonction rien addC(Card c):
|	|	this.c.add(c)
|	Fonction  entier addPts(): // On vérifie que la première vu que les 5 sont les mêmes
|	|	inspecter si this.c[0] :
|	|	|	cas  “Feet” : this.pts+=1; return 1; //Logique  du - au + rapide
|	|	|	cas “Bike” : this.pts+=2 ; return 2;
|	|	|	cas “Train”: this.pts+=4 ; return 4;
|	|	|	cas ”Car”: this.pts+=3 ; return 3;
|	|	|	cas ”Airplane”: this.pts+=5 ; return 5;
|	Fonction Card delC(Card c):
|	|	this.c.pop(c)
|	Fonction String toString(): // pour print le joueur sur le terminal
|	|	retourne (“Joueur n° ” + n.toString )

Structure Offer :
|	String stateOfOffer ; Player playerOr ; entier nbCards
|	Constructeur Offer(Player p, entier nb):
|	|	this.stateOfOffer=”noOffer” ; this.playerO = p; this.nbCards = nb;










Procédure player (Semaphore s, pack, Semaphore sG, Mutex lock, list[Offer] lsOff):
|	list c = [] //main du joueur
|	Pour i allant de 0 à 4 :
|	|	on lock : //Mutex lock 
|	|	|	c.add(pack.pop())
|	Tant que le jeu continue : //gameState == true:
|	|	println(“Hand of Player “ ,listPlayer[np].c)
|	|	int offr = entrée(“Want to make an offer : put a nbr btw 1
|	|	|	and”+string(nbPlayer)+”. If not put another nbr”)
|	|	on lock une nouvelle fois :
|	|	|	si offr entre 1 et nbPlayers: //nbPlayers étant 4
|	|	|	|	Card PlayerOffer=(“Which card?”) 
|	|	|	|	lsOff.add(PlayerOffer)
|	|	|	sinon, lsOff.add(0)
|	|	Boucle Pour permet de:
|	|	|	envoyer à tous les autres joueurs à part celui concerné :
|	|	|	|	sem[np des autres (à parcourir grâce à Pour].signal()
|	|	Pour i allant de 0 à nbPlayers-2 : //waiting for others offers 
|	|	|	sem[np].wait() //attente
|	|	srv = Thread(server(lsOff[np],c,
|
|

Procédure game (Offer offers ,Mutex lock , pack, list[Player] listPlayer):
|	Tant que le jeu continue : //par un boolean gameState == True
|	|	Pour le nombre de joueur:
|	|	|	semGame().wait  //semaphore pour attendre tout le monde		
|	|	Pour le nombre d’offre encore dans la liste des offres:
|	|	|	del listOffre[i]
|	|	Pour entier i allant de 0 à 3 :		
|	|	|	Si listPlayer[i] a gagné:
|	|	|	|	Afficher ("listPlayer[i] a déclaré avoir fini avec cette main 
|	|	|	|	:"+listPlayer[i].c+" il a engrengé"+listPlayer[i].addPts()+"
|	|	|	|	points")
|	|	|	|	Si listPlayer[i].pts>= plim:
|	|	|	|	|	Jeu s’arrête //notre boolean gameState <- false







Procédure serveur (Card offer,  listString[] hand,entier np,Card PlayerOffer):
|	global hand //global parceque sera utilisé après
|	global offer
|	Boucle infinie:
|	|	m, type=mq.receive()
|	|	Si type=0:		
|	|	|	mq.remove()
|	|	|	break
|        	|	Si type=np:
|           | 	|	offer.stateOfOffer="accepté"
|           | 	|	u=decode m //md
|           | 	|	u=Split(u)
|           | 	|	ProcessVisé=u[0]
|           | 	|	CarteRecu=u[1]
|           | 	Pour i allant de 0 au nb de carte offerte:
|           |     	|	hand.add(carteRecu)
|           | 	mq.send(PlayerOffer, type=ProcessVisé) //dans le message 
|           | 	k=0
|           | 	Pour i allant de 0 a hand.length())
|           |     	|	Si hand[i]=PlayerOffer:
|           |         	|	|	del han[i]
|           |        	|	|	 k=k+1
|           |    	|	 Si j=nombre d’offre:
|           |         	|	|	break



















Procédure client(Card offer, listString[] hand,Mutex lock):
|	global hand
|	print("Voici la liste des offres :", offre)
|    	offre(input("Interested? Write the number of offer to accept, or 0 to refuse all”)  
|     	Si offer se situe entre 0 et lsOff.lenth +1 :
|           |	offer=offer-1
|	|	on utilise le Mutex lock:
|	|	|	Si (listOffre[offre]!="accepted"):
|           |        	|	|	carte=exchangeC() // on implémentera cette fonction plus tard
|           |       	|	|	msg=carte+" "+os.getpid()
|           |         	|	|	msg = msg.encode()
|           |         	|	|	mq.send(msg,offers[offre].joueurSource)
|           |        	| 	|	m,t=mq.receive()
|           |        	| 	|	if t==os.getpid:
|           |           |  	|	|	msg=m.decode()
|           |           | 	|	|	Pour i allant de 0  à lsOff[offer].nb-1
|           |           |     	|	|	|	hand2.add(msg) //main temporaire
|	|	|	|	entier j =0;
|           |         	|	|	Pour i allant de 0 à la taille de la main hand -1:
|           |           |  	|	|	Si hand[i]==card:
|           |           |      	|	|	|	delC //fnction pour supprimer de la main
|           |           |     	|	|	 j++
|           |           |  	|	|	Si j==lsOff[offer].nb:
|           |           |      	|	|	|	break quitter la boucle pour
|           |     	|	|	Pour i allant de 0 aux nombre d’offres -1):
|           |         	|	|	|	quit=""
|           |         	|	|	|	quit=quit.encode()
|           |         	|	|	|	mq.send(quit,i)
|	|	|	Sinon:
|	|	|	|	|	print("Dommage une offre a déjà été acceptée")













Dans notre MAIN PROGRAM (là on tout sera lancé et implémenté):
On utilise un Manager de thread et Processus nommé Manager (//used on TD)
avec notre Manager() nommé manage par la suiter:
|	boolean gameState=True //utilisé dans les procdéudres précdente
|	sem=[]
|	listCard[] offers=[]
|	list[Player] listPlayer=Liste de tous les joueurs à implémenter
|	Pour i allant de 0 à nombre de Joueurs -1:
|	|	s.add(0) //sem
|	Mutex lock=Lock()
|	nbPlayer=4	
|	pack= manager.list() //pack de cartes
|           list[Card] listOffre=[]
|	Pour i allant de 0 :
|	|	pack.add(Carte("Car"))
|	|	pack.add(Carte("Train"))
|	|	pack.add(Carte("Airplane"))
|	random.shuffle(pack) // on melange le pack
|	players = (Process(player(pack,lsOff,sem,semGame,lock) in range(nbPlayer))
|      	game = Process(game(offers,lock,pack,listPlayers,semGame))
|	game.start()
|	Pour une joueur i parmi les joueurs du tableau players:
|       	i.start()
|	game.join()
|       	Pour un joueur i parmi les joueurs du tableau players:
|      		i.join()


'''