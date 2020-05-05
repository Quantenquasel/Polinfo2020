# -*- coding: utf-8 -*-
"""
Autor: A.K.
Programmcode:
SHA256 – Werte mit führendem Nullen finden
Beschreibung
Das nachfolgende Programm rechnet solange SHA256 - Hashwerte aus, bis die angegebene Anzahl führender Nullen erreicht ist.
Die Rechenzeit wird in eine Textdatei geschrieben. 
"""
import hashlib
import time
import datetime
import sys
repeat = 1
differ = 0#Variable dient der Zeitspannenberechnung
print("Das Programm rechnet solange SHA256 - Hashwerte\nbis mindestens die angegebene Anzahl führender Nullen erreicht ist.\nDie Rechenzeit wird in eine Textdatei geschrieben. (A.K.)")
print()
with open("Mining_Simulation.txt", "a") as e:#Ergebnisdatei erzeugen und Ergebnis jeweils hinzufügen
    while repeat:
        Zähler = 0
        Treffer = 0
        s = int(input("Geben Sie die Anzahl der führenden Nullen des SHA256-Hashwertes an:"))
        startzeit = time.time()#Stoppuhr starten
        print(startzeit)
        while Treffer == 0:
            hash_256 = hashlib.sha256(str(Zähler).encode()).hexdigest()
            if hash_256[:s] == s*"0":#Bedingung für führende Nullen
                print(hash_256)
                endezeit = time.time()#Stoppuhr anhalten
                print(endezeit)
                differ = endezeit - startzeit#Berechnungszeit errechnen
                print("Berechnungszeit:",differ)
                e.write("Für die Berechnung eines SHA256-Haswertes mit " + str(s) + "   führenden Nullen wurden " + str(Zähler) + " Durchläufe " + str(differ/60) + " Minuten benötigt.")#Ergebnis in die Ergebnisdatei schreiben
                e.write("\n\n")
                e.write(hash_256)
                e.write("\n\n")
                Treffer = 1
            Zähler +=1
        repeat= input("Zum Beenden die enter-Taste und für einen weiteren Durchlauf ein andere Taste und die enter-Taste drücken.")
print()
print("Nach: ", Zähler, " Hashberechnungen wurde ein SHA256 gefunden, der mindestens ",s," führen-de Nullen hat: \n\n ",hash_256 )
