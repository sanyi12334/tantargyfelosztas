# 1. feladat
# Olvassa be és tárolja el a beosztas.txt állományban talált adatokat, és annak
# felhasználásával oldja meg a következő feladatokat!

beosztas={}
beosztasok=[]
seged_lista=[]

with open("beosztas.txt","r",encoding="utf-8") as fm1:
    for sor in fm1:
        seged_lista.append(sor.strip())
        if len(seged_lista)==4:
            beosztas["tanar"]=seged_lista[0]
            beosztas["tantargy"]=seged_lista[1]
            beosztas["osztaly"]=seged_lista[2]
            beosztas["oraszam"]=int(seged_lista[3])
            beosztasok.append(beosztas)
            seged_lista=[]
            beosztas={}

# 2. feladat
# Hány bejegyzés található az állományban? Az eredményt írassa ki a képernyőre!

print("2. feladat")
print(f"A fájlban {len(beosztasok)} bejegyzés van.")

# 3. feladat
# Mennyi a heti óraszám az iskolában? Az eredményt írassa ki a képernyőre!

def osszegzes(bok):
    osszeg=0
    for elem in bok:
        osszeg+=elem["oraszam"]
    return osszeg

print("3. feladat")
print(f"Az iskolában a heti összóraszám: {osszegzes(beosztasok)}")

# 4. feladat
# Kérje be a felhasználótól egy tanár nevét, és írassa ki a képernyőre, hogy hetente hány
# órában tanít!

print("4. feladat")
be_tanarnev=input("Egy tanár neve= ") or "Albatrosz Aladin"

def tanar_oraszamamnak_osszegzese(bok,be_nev):
    osszeg=0
    for elem in bok:
        if be_nev==elem["tanar"]:
            osszeg+=elem["oraszam"]
    return osszeg

print(f"A tanár heti óraszáma: {tanar_oraszamamnak_osszegzese(beosztasok,be_tanarnev)}")

# 5. feladat
# Készítse el az of.txt fájlt, amely az osztályfőnökök nevét tartalmazza osztályonként
# az alábbi formában (az osztályok megjelenítésének sorrendje a mintától eltérhet):
#kiválogatás

with open("of.txt","w",encoding="utf-8") as fm2:
    for beosztas in beosztasok:
        if beosztas["tantargy"]=="osztalyfonoki":
            print(f"{beosztas['osztaly']} - {beosztas['tanar']}",file=fm2)


# 6. feladat
# Egyes osztályokban bizonyos tantárgyakat a tanulók csoportbontásban tanulnak: ekkor az
# adott tantárgyra és osztályra két bejegyzést is tartalmaz a tantárgyfelosztás. Kérje be egy
# osztály azonosítóját, valamint egy tantárgy nevét, és írassa ki a képernyőre, hogy az adott
# osztály a megadott tantárgyat csoportbontásban vagy osztályszinten tanulja-e!
# (Feltételezheti, hogy a megadott osztály tanulja a megadott tantárgyat.) 


print("6. feladat")
be_osztaly=input("Osztály= ") or "10.b"
be_tantargy=input("Tantárgy= ") or "kemia"


def csoportban_tanuljak(beo, be_o, be_t):
    i=0
    while i<len(be_o) and not(beo[i]["osztaly"]==be_o):
        i+=1
    return not(i<len(beo))

if csoportban_tanuljak(beosztasok, be_osztaly, be_tanarnev):
    print(f"Csoportbontásban tanulják.")
else:
    print(f"osztályszinten tanulják.")


# 7. feladat
# A fenntartó számára az is fontos információ, hogy hány tanár dolgozik az iskolában. Írassa
# ki ezt az adatot a képernyőre!

print("7. feladat")

tanarok=[]

for beosztas in beosztasok:
    if beosztas["tanar"] not in tanarok:
        tanarok.append(beosztas["tanar"])

print(f"Az iskolában {len(tanarok)} tanár tanít.")