#Aufgabe 1
zahl = int(input("Geben Sie eine Zahl ein: "))
if zahl < 0:
    print("Die Zahl ist negativ.")
elif zahl > 0:
    print("Die Zahl ist positiv.")
else:
    print("Die Zahl ist 0.")

#Aufgabe 2
uhrzeit = int(input("Geben Sie die Uhrzeit ein: "))
if uhrzeit < 7 or uhrzeit >= 23:
    print("Schlafenszeit!")
else:
    print("Sonne Tanken!")	

#Aufgabe 4
uhrzeit = int(input("Geben Sie die Uhrzeit ein: "))
print("Es ist",uhrzeit,"Uhr da bin ich gerade am:")

if uhrzeit < 7:print("Schlafen")
elif uhrzeit < 8:print("Arbeiten")
elif uhrzeit > 13 and uhrzeit < 14:print("Mittagessen")
elif uhrzeit < 17:print("zocken")  
elif uhrzeit < 22:print("serien schauen")
else:print("Schlafen")

#Aufgabe 5
