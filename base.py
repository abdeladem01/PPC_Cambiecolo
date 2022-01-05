
class Joueur:
	def __init__(self, numero, hand): # On lui attribue un numéro et une liste de cartes
		self.numero=numero
		self.hand=hand
		self.points=0
	def addCard (self,carte): # On peut ajouter une carte à sa main
		self.hand.append(carte)
	def print(self): # Fonction print
		print("Joueur", self.numero)	
	def checkWin(self): # Checker s"il peut gagner la partie
		return len(set(self.hand))==1:
	def addPoint(self)
		if self.hand[0]="Shoes":
			self.points=self.points+5
			return 5
		if self.hand[0]="Bike":
			self.points=self.points+4
			return 4
		if self.hand[0]="Train":
			self.points=self.points+3
			return 3
		if self.hand[0]="Car":
			self.points=self.points+2
			return 2
		if self.hand[0]="Airplane":
			self.points=self.points+1
			return 1

class Offre:
	def __init__(self, joueurSource, nb):   # Statut de l'offre, joueur qui propose et recoit, cartes mises dans l'offre
		self.state="blank"
		self.joueurSource=joueurSource
		self.nb	= nb	


key = 128 
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREAT)



def game(offers,lock,deck,listJoueur)

    while (gameContinues):

		for _ in range(nbJoueur):	# On attend que tous les joueurs ai finit d'accepter des offres pour reset l'état des offres
			semGame().wait			
		for i in range(listOffre.length):
			del listOffre[i]
			

		if(listeJoueur[0].checkWin()):
			print("Le joueur 0 a sonné la cloche avec cette main :"+listeJoueur[0].hand+" il a marqué "+listeJoueur[0].addPoint()+" points")
			if listeJoueur[0].point>= ptsLimites:
				gameContinues=False
		if(listeJoueur[1].checkWin()):
			print("Le joueur 1 a sonné la cloche avec cette main :"+listeJoueur[1].hand+" il a marqué "+listeJoueur[1].addPoint()+" points")
			if listeJoueur[1].point>= ptsLimites:
				gameContinues=False
		if(listeJoueur[2].checkWin()):
			print("Le joueur 2 a sonné la cloche avec cette main :"+listeJoueur[2].hand+" il a marqué "+listeJoueur[2].addPoint()+" points")
			if listeJoueur[2].point>= ptsLimites:
				gameContinues=False
		
		
       
def player(deck,listOffre,sem,semGame,lock)
    hand=[]
	for i in range(5):
		with lock:
			hand = hand+deck.pop()) #On tire une carte
	while(gameContinues):
		print("Ceci est votre main actuelle : ",listeJoueur[numJoueur].hand)
		offre=int(input("Voulez vous faire une offre ? \n Tapez un nombre entre 1 et"+nbJoueurs+ "pour faire une offre de la valeur correspondante \n Tapez 0 ou "+nbJoueurs+" et plus si vous ne souhaitez pas faire d'offre")) 
		with lock:
            if 0<offre<4:
                monOffre=input("Quel type de carte offrez vous")
				listOffre.append(offre)
            else:
                listOffre.append(0)

		for i in range(nbJoueurs):
			if	((numJoueur+i)%nbJoueurs!=numJoueur):
				sem[(numJoueur+i)%nbJoueurs].signal()
		for i in range(nbJoueurs-1):   #On attend que tous les joueurs ai fini de faire leurs offres
			print("En attente des "+nbJoueurs-1-i+ "autres joueurs")
			sem[numJoueurs].wait
        
        server = Thread(target=server, args=(listOffre[numJoueur],hand,numJoueur,monOffre)
        client = Thread(target=client, args =(listOffre,hand,lock))
		server.start()
        client.start()
        server.join()
        client.join()
		semGame().signal
		

def server(offer,hand,numJoueur,monOffre):
    global hand
    global offers
    while True:
        m, t=mq.receive()
        if t==0:
			
			mq.remove()
			break
        if t==numJoueur:
            offer="accepted"
            x=m.decode()
            x=x.split()
            targetPid=x[0]
            cardReceived=x[1]
            for i in range(offer.nb)
                hand.append(cardReceived)
            mq.send(monOffre, type=targetPid)
            j=0
            for i in range (hand.length()):
                if hand[i]==monOffre:
                    del hand[i]
                    j++
                if j==offer.nb:
                    break
            
            
def client(offers,hand,lock):
    global hand
    print("Voici la liste des offres :", offers)
		offre(int(input("Voulez vous accepter une offre ?\n Tapez le numéro de l'offre que vous souhaitez accepter \n Attention ! Taper 1 choisira la première offre et taper 0 déclinera les offres")))
		if 0<offre<listOffre.length+1:
            offre=offre-1
			with lock:
				if(listOffre[offre]!="accepted"):
                    carte=choixDeCarteAEchanger()
                    msg=carte+" "+os.getpid()
                    msg = msg.encode()
                    mq.send(msg,offers[offre].joueurSource)
                    m,t=mq.receive()
                    if t==os.getpid
                        msg=m.decode()
                        for i in range(offers.[offre].nb)
                            hand2.append(msg)

                    for i in range (hand.length()):
                        if hand[i]==carte:
                            del hand[i]
                            j++
                        if j==offers[offre].nb:
                            break
                for i in range(offers.length[]):
                    quit=""
                    quit=quit.encode()
                    mq.send(quit,i)

				else:
					print("Dommage une offre a déjà été acceptée")



if __name__ == "__main__":

	with Manager() as manager:
		gameContinues=True
		sem=[]
		offers=[]
		listJoueur=instancieListJoueur()
		for i in range(ListJoueur.length()):
			sem.append[0]
		lock=Lock()
		nbJoueur=3
		# On ajoute les cartes à la pioche	
		deck = manager.list()
        listOffre=[]
		for i in range(5):
			deck.append(Carte("Voiture"))
			deck.append(Carte("Bateau"))
			deck.append(Carte("Avion"))
		random.shuffle(deck)
	
		players = (Process(target=player, args=(deck,listOffre,sem,semGame,lock) in range(nbJoueur))
        game = Process(target=game, args =(offers,lock,deck,listJoueur,semGame))
		game.start()
		for i in players:
        	i.start()
		game.join()
        for i in players:
        	i.join()