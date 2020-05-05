# -*- coding: utf-8 -*-
"""
@author: A.K.
Berechnung der 64 "Rundenkonstanten" nach NIST
"""
import math
Liste =[]
Konstantenliste=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,
                  211,223,227, 229, 233,239,241, 251,257,263,269,271,277,281,283,293,307,311]#Die ersten 64 Primzahlen
print()
print('Liste der ersten',len(Konstantenliste),' Primzahlen:\n\n',Konstantenliste)
print()
r = 1
for s in Konstantenliste:
    t = pow(s,1/3)
    t_Vorkomma = math.trunc(t)#Bestimmung der Vorkommazahl
    t = t-t_Vorkomma#t ist jetzt < 1 !!
    print("Die ",r," -te Primzahl lautet: ",s,". Ihre Nachkommastellen lauten: ",t)
    print()
    t *= 2**32
    t2= hex(int(t))
    print("Der 32-bittige Nachkommateil der 3-ten Wurzel aus",s," in Hexadezimaldarstellung lautet: ", t2)
    Liste.append(t2)
    print()
    r += 1
print(Liste)
Primzahl_Nachkomm_hex = zip(Konstantenliste,Liste)
Primzahl_Nachkomm_hex_dict = dict(Primzahl_Nachkomm_hex)
Dictonaryliste = Primzahl_Nachkomm_hex_dict.items()
print()
print(Primzahl_Nachkomm_hex_dict)
SHA256_Konstanten64 = open("SHA256_Konstanten64.txt","w")#(name + ".txt", "w")
for i in Liste:
    SHA256_Konstanten64.write(str(i) + ";")
SHA256_Konstanten64.write(str("\n\n"))
for z in Dictonaryliste:
    SHA256_Konstanten64.write(str(z) + "\n")
SHA256_Konstanten64.close()
#Vergleich mit NIST




    
