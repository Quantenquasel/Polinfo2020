#Bitcoins - Anzahl
Anzahl = 0# keine Bitcoins vorhanden
Bl = 0
Summe =0
k = 210000
f = 1/2
for x in range(30):
    Bel =50
    Bel=Bel*f**x
    s = k*x
    for i in range(k):
        Summe +=Bel
    print ("Anzahl: ",k," Blöcke ","-Belohnung pro Block: ",Bel,"Summe aller Blöcke: ",s," Summe aller Bitcoins: ", Summe," Bitcoins",)
print("Anzahl: ",Anzahl," Blöcke - errechnete SHA256: ", 30*210000)