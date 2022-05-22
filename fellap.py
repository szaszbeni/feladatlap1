from math import* 
from random import*
mondat=input("Kérek egy mondatot!")
print(len(mondat))
print("A szoveg karaktereinek szama!",len(mondat)) 

betu=input()
if betu in mondat:
    print("Van benne")
else:
    print("Nincs benne")

def megszamol(kar,szoveg):
    return szoveg.count(kar)
print("A mondatban a karakter elofordulasanak a szama:",megszamol(betu,mondat))

def leghosszabb(mondat):
    szavak=mondat.split(" ")
    q=darabok[0]
    for item in darabok:
        if len(q)>len(item):
            q=item
        return q
        print("A leghosszabb szo",leghosszabb(mondat))
        
    w=float(input("Add meg az ábrát"))
    print("kor kerulete", w*pi)
    print("terulet",row(w(2,2)*pi))

    szamok =[]
    for i in range(20):
        szamok.append(randint(-40,40))

def valogat(lista):
    list1=[]
    list2=[]
    for item in lista:
        if item%5==0:
            list1.append(item)
        else:
            list2.append(item)

    print("5tel oszthato")
    for item in list1:
        print(item, end=" ")
    print(" ")
    print("5el nem oszthato")
    for item in list2:
        print(item, end=" ")

def ajto():
    f=open("ajto.txt", "r")
    beolvas=f.readlines()
    f.close()
    adatok=[]
    for item in beolvas:
        adatok.append(Ajto(item))
        print(len(adatok))
        print("Az elsö belepö:", adatok[0])
    for i in range(len(adatok)-1,-1,-1):
        if adatok[i].irany =="ki":
            print("Az utolso kilepo", adatok[i])
            break

def ajto2():
    f=open("ajto.txt","r")
    osszes=f.read()
    be=osszes.count("be")
    ki=osszes.count("ki")
    print("A tarsalgoban", be-ki)

def azonosito():
    azonosito=int(input())
    for item in a:
        if item.irany=="be":
            print(item.ora + item.perc + "+")
        else:
            print(item.ora + item.perc)

megszamol(kar,szoveg)
leghosszabb(mondat)
valogat(lista)
ajto()
ajto2()

