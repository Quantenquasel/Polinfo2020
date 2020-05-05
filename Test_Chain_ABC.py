# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 16:46:18 2020

@author: A.K.
"""
import time
import hashlib
import copy
import random
class Block:
    def __init__(self,Bezeichnung, Datum):
        pass
Bezeichnung = [chr(i) for i in range(65,91)]#ASCII Großbuchstaben
print(Bezeichnung)
L = []
def Block():
    L = []
    for i in Bezeichnung:
        z = random.choice(Bezeichnung)
        t = int(time.time())
        B = random.randint(1,10)
        s = hashlib.sha256((i+z+str(B)+str(t)).encode()).hexdigest()
        L.append((t,i,z,B,s))
        print(("Zeitpunkt:",t,"Sender:",i,"Empfänger:",z,"Betrag: ",B,"SHA256(Zeitpunkt, Sender, Empfänger,Betrag):",s))
        time.sleep(1)#kleiner als 1 Sekunde führt zu übereinstimmenden Zeitpunkten
    L_hash = hashlib.sha256((str(L)).encode()).hexdigest()
    print()
    print("Blockhash:",L_hash,"Anzahl der Transaktionen innerhalb des Blocks: ",len(L))
    with open("Chain.txt","a") as C:
        C.write("B1:\n\n"+str(L))
        C.write("Blockhash:"+L_hash)
    print()
    print(L)
B1 = Block()
L_Blöcke = []
L_Blöcke.append(B1)
L_Blöcke1 = copy.deepcopy(L_Blöcke)
L_Blöcke1.append(B1)
L_Namen = ['Andreas','Bertram','Claudia','Dora','Eva']
L_Namen_pseudo=[]
print()
for i in L_Namen:
    t = hashlib.sha256(i.encode()).hexdigest()
    L_Namen_pseudo.append(t)
print(L_Namen_pseudo)
Namen_Pseudo = list(zip(L_Namen, L_Namen_pseudo))#mit zip allein: <zip object at 0x000001540FEA4A88>
print(Namen_Pseudo)

print("Zufallswahl aus der Liste: ", random.choice(Bezeichnung))