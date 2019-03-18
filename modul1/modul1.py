print ("NAMA : Sartika Rizki M")
print ("NIM  : L200170118")
print ("KELAS: C ")
print ("MODUL: 1")


print ("-----------------------------NOMER 1 ---------------------------------")
def cetakSiku(x):
    for i in range(1, x+1):
        print("*"*i)

cetakSiku(5)

print ("-----------------------------NOMER 2 ---------------------------------")


def gambarlahPersegiEmpat(p, l):
    for i in range(1, p+1):
        if i==1 or i==p:
            print("@"*l)
        else:
            print("@"+" "*(l-2)+"@")

gambarlahPersegiEmpat(8, 10)

print ("-----------------------------NOMER 3 ---------------------------------")

def jumlahHurufVokal(input):
    total = 0
    voc = ["a", "i", "u", "e", "o"]
    for A in input:
        if A in voc:
            total+=1
    return [len(input), total]

def jumlahHurufKonsonan(input):
    total = 0
    voc = ["a", "i", "u", "e", "o"]
    for A in input:
        if A in voc:
            total+=1
    return [len(input), len(input)-total]

v = jumlahHurufVokal("Surakarta")
k = jumlahHurufKonsonan("Surakarta")

print(v)
print(k)

print ("-----------------------------NOMER 4 ---------------------------------")

def rerata(b):
    return sum(b)/len(b)
print ("rerata([1,2,3,4,5])")
print (rerata([1,2,3,4,5]))

g = ([3,4,5,4,3,4,5,2,2,10,11,23])
print("rerata(g)")
print(rerata(g))

print ("-----------------------------NOMER 5 ---------------------------------")
from math import sqrt as sq
def apakahPrima(n):
    n =  int(n)
    assert n >=0
    primaKecil = [2, 3, 5, 7, 11]
    bukanPrKecil = [0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%i == 0:
                return False
                break
        else :
            return True
print ("apakahPrima(17)")     
print (apakahPrima(17))

print ("apakahPrima(97)")
print (apakahPrima(97))

print ("apakahPrima(123)")
print (apakahPrima(123))

print ("-----------------------------NOMER 6 ---------------------------------")
from math import sqrt as sq
def apakahPrima(n):
    n =  int(n)
    assert n >=0
    primaKecil = [2, 3, 5, 7, 11]
    bukanPrKecil = [0, 1, 4, 6, 8, 9, 10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else:
        for i in range(2,int(sq(n))+1):
            if n%i == 0:
                return False
                break
        else :
            return True
        
for i in range(2, 1001):
    print(str(i)+" "+str(apakahPrima(i)))

print ("-----------------------------NOMER 7 ---------------------------------")
import functools
import operator

def faktorPrima(n):
    n_ori = n
    pri = []
    st = True
    while st:
        for i in range(2, n+1):
            if n/i == int(n/i):
                pri.append(i)
                n = int(n/i)
                break
        if functools.reduce(operator.mul, pri, 1) == n_ori:
            st = False
    return pri

print(faktorPrima(10))
print(faktorPrima(120))
print(faktorPrima(19))

print ("-----------------------------NOMER 8 ---------------------------------")
def apakahTerkandung(a,b):
    return a in b

h = "do"
k = "Indonesia tanah air beta"
print(apakahTerkandung(h, k))
print(apakahTerkandung("pusaka", k))

print ("-----------------------------NOMER 9 ---------------------------------")
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("Python UMS")
    elif i%3==0:
        print("Python")
    elif i%5==0:
        print("UMS")
    else:
        print(i)

print ("-----------------------------NOMER 10 --------------------------------")
from math import sqrt as akar

def selesaikanABC(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D < 0:
        return "Determinannya negatif. Persamaan tidak mempunyai akar real."
    else:
        x1 = (-b + akar(D))/(2*a)
        x2 = (-b - akar(D))/(2*a)
        hasil = (x1, x2)
        return hasil
print (selesaikanABC(1,2,3))


print ("-----------------------------NOMER 11 --------------------------------")
def apakahKabisat(n):
    if n%4==0:
        if n%100==0 and n%400==0:
            return True
        elif n%100==0 and n%400!=0:
            return False
        return True
    return False

print(apakahKabisat(1896))
print(apakahKabisat(1897))
print(apakahKabisat(1900))
print(apakahKabisat(2000))
print(apakahKabisat(2004))
print(apakahKabisat(2100))
print(apakahKabisat(2400))


print ("-----------------------------NOMER 12 --------------------------------")
from random import randint

tebak = randint(1, 100)
print("Permainan tebak angka.")
print("Saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak.")
i = 1
gameOver = True
while i <= 3 :
    a = int(input("Masukkan tebakan ke-"+str(i)+" :> "))
    if a == tebak:
        print("Ya. Anda benar")
        gameOver = False
        break
    else:
        if a <= tebak:
            print("Itu terlalu kecil. Coba lagi")
        else:
            print("Itu terlalu besar. Coba lagi")
    i = i+1
if gameOver:
    print("Permainan selesai")

print ("-----------------------------NOMER 1 ---------------------------------")
def Katakan(angka):
    satuan = ["satu", "dua", "tiga", "empat", "lima",
              "enam", "tujuh", "delapan", "sembilan", "sepuluh",
              "sebelas", "dua belas", "tiga belas", "empat belas", "lima belas",
              "enam belas", "tujuh belas", "delapan belas", "sembilan belas"
              ]
    angka = '{:0,.0f}'.format(int(angka))
    angka = angka.split(",")
    katakan = []
    idx = 1
    for x in angka[::-1]:
        seribu = False
        if idx == 2 and x[-1]!="0":
            if int(x)< 2 :
                katakan.append("seribu")
                seribu = True
            else:
                katakan.append("ribu")
        if idx == 3 and x[-1]!="0":
            katakan.append("juta")
        if seribu == False:
            if int(x[-2:])<20 and int(x[-2:])>0:
                katakan.append(satuan[int(x[-2:])-1])
            elif int(x[-2:])>0:
                if int(x[-1])!=0:
                    katakan.append(satuan[int(x[-1])-1])
                if int(x[-2]) != 0:
                    katakan.append(satuan[int(x[-2])-1]+" puluh")
        if int(x[0]) > 2 and len(x)==3 :
            katakan.append(satuan[int(x[0])-1]+" ratus")
        elif len(x)==3 and int(x[0])!=0 :
            katakan.append("seratus")
        idx+=1
    return " ".join(katakan[::-1])

print(Katakan(3125750))

print ("//////////////////////////////NOMER 14////////////////////////////////")

def formatRupiah(num):
    a = "Rp {:,}".format(num)
    return ".".join(a.split(","))

print(formatRupiah(1500))
print(formatRupiah(2560000))
