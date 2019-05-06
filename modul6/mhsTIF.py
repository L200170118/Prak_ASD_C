class mhsTIF (object):
    def __init__ (self, nama, nim, kota, us):
        self.nama = nama
        self.nim = nim
        self.kt = kota
        self.us = us
    def __str__(self):
        s = self.nama + ", NIM " +str(self.nim) + " Alamat " +self.kt + \
            " jumlah uang saku " + str(self.us) + " per bulan."
        return s
    def getnim (self):
        return self.nim

m1 = mhsTIF ("Sartika", 118, "solo", 1200000)
m2 = mhsTIF ("Fitri", 110, "ngawi", 1254000)
m3 = mhsTIF ("Windis", 115, "pemalang", 128700)
m4 = mhsTIF ("Agatha", 127, "purwodadi", 117000)
m5 = mhsTIF ("Afgant", 117, "solo", 1300000)

Daftar = [m1, m2, m3, m4, m5]

def mergesort(A):
    if len (A) > 1 :
        mid = len(A) //2
        separuhKiri = A[:mid]
        separuhKanan = A [mid:]

        mergesort (separuhKiri)
        mergesort (separuhKanan)

        i=0;j=0;k=0
        while i < len (separuhKiri)and j < len (separuhKanan) :
            if separuhKiri[i].nim < separuhKanan[j].nim :
                A[k].nim = separuhKiri[i].nim
                i = i+1
            else :
                A[k].nim = separuhKanan[j].nim
                j = j+1
            k = k+1

        while i < len (separuhKiri):
            A[k].nim = separuhKiri[i].nim
            i = i+1
            k = k+1
            
        while j < len (separuhKanan):
            A[k].nim = separuhKanan[j].nim
            j = j+1
            k = k+1

        return A
    
def quickSort(A):
    quickSortBantu (A,0, len(A) -1)
    return A

def quickSortBantu(A, awal, akhir):
    if awal < akhir :
        titikBelah = partisi(A, awal, akhir)
        quickSortBantu(A, awal, titikBelah -1)
        quickSortBantu(A, titikBelah +1, akhir)

def partisi(A, awal, akhir):
    nilaiPivot = A[awal].getnim()

    penandaKiri = awal +1
    penandaKanan = akhir

    selesai = False
    while not selesai :
        while penandaKiri <= penandaKanan and \
              A[penandaKiri].getnim() <= nilaiPivot :
            penandaKiri +=1

        while A[penandaKanan].getnim() <= nilaiPivot and\
              penandaKanan >= penandaKiri :
            penandaKanan -=1

        if penandaKanan < penandaKiri :
            selesai = True
        else :
            temp = A[penandaKiri]
            A[penandaKiri] = A[penandaKanan]
            A[penandaKanan] = temp

    temp = A[awal]
    A[awal] = A[penandaKanan]
    A[penandaKanan] = temp

    return penandaKanan

mergesort(Daftar)
for i in Daftar:
    print (i)

quickSort(Daftar)
for i in Daftar:
    print (i)
    
