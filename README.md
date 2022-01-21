# PROJET PPC - CAMBIECOLO - v.2022
## Programmation Parallèle et Concurrente (Python Approach)
###### written by Fattah Abdeladem Saoud 

### 1. What is Cambiecolo
  Cambiecolo is the environmentalist cousin of the Cambio card game. Its goal is presenting a hand of 5
cards of the same transport means. The player who succeeds is awarded the points of the transport they
put together. The game deals as many different types of transports as there are players. Possible transport
means are: airplane, car, train, bike and shoes. Each player receives 5 random cards, face down, e.g. if there
are 3 players, 15 cards of 3 transport means are distributed, 5 cards per transport. A bell is placed in the
middle of the players. As soon as cards are distributed, players start exchanging by announcing the
number of cards they offer, from 1 to 3 identical cards, without showing them. They exchange the same
number of cards with the first player to accept the offer. This continues until one of the players rings the
bell and presents a hand of 5 identical cards, scoring the points of the transport they have grouped. 

### 2. How to launch the project?
  First launch the file : remoteSM.py (it is the remote class that manage the shared memory)
   Then launch the server : serverSM.py (and enter the number n of players you want)
   Finally, launch a bunch of client (but only the first n players will be accepted)
   THEN ENJOY!
The Game can be played in different computers as the BaseManager class permits it. 
All you have to do is to edit in the three files the adresss and the port (8888 for TCP) and the authkey:

(Change it in :
  line 39 for remoteSM.py
  line 15 for serverSM.py
  line 19 for clientSM.py
)



###### Group : Abdeladem Saoud Fattah | Paul Bridon

