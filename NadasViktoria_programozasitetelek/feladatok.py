import random
import math
"""
Írj eljárást, mely a paraméterében kap két számot
ezen két egész szám közötti (a határértékek is bele számítanak) páros számok összegét számolja ki
"""
def elsoFeladat(min:int, max:int):
    i:int = min
    osszeg:int = 0
    while i <= max:
        if i%2==0:
            print(i)
            osszeg +=i
        i+=1
        # elágazás vége
    #ciklus vége
    #visszatérési érték
    return osszeg       #ez egy fgv, aminek van viszatérési értéke, vagyis eredménye

def negativ_db():
    i:int = 0
    db:int = 0
    while i<20:
        szam:int=math.floor(random.random()*21-10)
        print(szam)
        if szam < 0:
            db += 1
        i+=1
        #elágazás vége
    #ciklus vége
    ##visszatérési érték
    return db

def negativ2():
    db:int=0
    for i in range(0,2,1):
        szam:int=math.floor(random.random()*21-10)
        print(szam)
        if szam < 0:
            db += 1


def ujraElsoFeladat(min:int, max:int):
    osszeg:int = 0

    for i in range(min, max, 1):
        if i%2==0:
            osszeg +=i
    return osszeg


"""
Írj fgvnyt, amely generál 10 db véletlen számot,
12 és 33 között zárt intervallumban, és visszatér ezek összegével
"""
def veletlen():
    osszeg:int = 0
    for i in range(0, 10, 1):
        szam:int = math.floor(random.random()*(34-12)+12)
        osszeg+= szam
    return osszeg

"""
Írj fgvnyt, amely generál 8 db véletlen számot,
[20, 50) intervallumban, és visszatér ezek közül a legnagyobb számmal
"""

def nyolcVeletlen():
    vmi:int = 0
    for i in range(0, 8, 1):
        szam:int = math.floor(random.random()*(50-20)+20)
        if szam > vmi:
            vmi=szam
    return vmi

"""
Kérjünk be 3db egész számot a felhasználótól
mekkora a számok átlaga?
"""
def egesz_beker():
    osszeg:int = 0
    for i in range (0,3,1):
        szam:int = int(input(f"Kérem az {i+1}. egész számot: "))
        osszeg += szam
    return osszeg/3


"""
Kérjünk be egész számokat a felhasználótól, amíg 0-t nem ad.
Írjuk ki a számok átlagát.
"""

def egesz():
    """szam = int(input("Adj meg egy egész számot: "))
    tobbiSzam=0
    while szam != 0:
        tobbiSzam += szam
        szam = int(input("Adj meg egy egész számot: "))
    if szam == 0:
        atlag = tobbiSzam/len(tobbiSzam)

    print(atlag)"""
    osszeg:int=0
    i:int=0
    db:int=0
    szam:int = int(input(f"Kérem az {i+1}. egész számot"))
    while szam != 0:
        osszeg += szam
        db += 1
        i += 1
        szam:int = int(input(f"Kérem az {i+1}. egész számot"))
    return osszeg