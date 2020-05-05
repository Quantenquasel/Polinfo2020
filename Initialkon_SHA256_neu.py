# -*- coding: utf-8 -*-
"""
@author: A.K.
Berechnet die 8 Initialkonstanten zur Berechnung von SHA256 _werten nach : NIST
"""
import math
Liste =[]
Primzahl_Nachkomma_hex ={}
Konstantenliste=[2,3,5,7,11,13,17,19]#Die ersten 8 Primzahlen
print()
print(Konstantenliste,": In der Liste sind ",len(Konstantenliste)," Primzahlen.")
print()
r = 1
for s in Konstantenliste:
    t = math.sqrt(s)#Wurzel ziehen
    t_Vorkomma = math.trunc(t)#Bestimmung der Vorkommazahl
    t = t-t_Vorkomma#t ist jetzt < 1 !!
    print("Die ",r," -te Primzahl lautet: ",s,". Ihr 32-bittiger Nachkommateil der Quadratwurzel lautet: ",t)
    print()
    t *= 2**32
    t2= hex(int(t))
    print("Der 32-bittige Nachkommateil in Hexadezimaldarstellung lautet: ", t2)
    Liste.append(t2)
    print()
    r += 1
print('Initialkonstantenliste:\n\n ',Liste)
Primzahl_Nachkomm_hex = dict(zip(Konstantenliste,Liste))
print()
print('Primzahlen und Initialkonstanten als Dictionary:\n\n',Primzahl_Nachkomm_hex)
print()
with open("SHA256_Inikonst8.txt","w") as SHA256_IniK:#Ergebnisse in eine Datei schreiben
    SHA256_IniK.write(str(Primzahl_Nachkomm_hex)+"\n\n")
    for z in Primzahl_Nachkomm_hex:
        SHA256_IniK.write(str(z) + "\n")
