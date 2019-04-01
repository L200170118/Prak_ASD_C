class MhsTIF(object):
    def __init__(self, nim):
        self.nim = nim

    def __str__(self):
        a = 'nim' + str(self.nim)
        return a

    def getlNim (self) :
        return self.nim

c0 = MhsTIF(10)
c1 = MhsTIF(14)
c2 = MhsTIF(12)
c3 = MhsTIF(21)
c4 = MhsTIF(24)
c5 = MhsTIF(65)
c6 = MhsTIF(11)
c7 = MhsTIF(43)
c8 = MhsTIF(56)
c9 = MhsTIF(60)
c10 = MhsTIF(20)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def swap(A, p, q):
    tmp  = A[p]
    A[p] = A[q]
    A[q] = tmp
    
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai.nim < A[pos -1].nim:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

def cetakDaftar(d) :
    for i in d:
        print (i) 

insertionSort(Daftar)
cetakDaftar(Daftar)

#2
def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos -1]:
            A[pos] = A[pos -1]
            pos = pos -1
        A[pos] = nilai

A = [1,2,3,4,5,6,7,8,9,10]
B = [11,12,13,14,15,16,17,18,19,20]
C = []
C.extend(A)
C.extend(B)
insertionSort(C)
print ('\n Nilai C: ',C)

#3

def swap(A,p,q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini+1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A,j,j+1)
                
def selectionsort(A):
    n = len(A)
    for i in range (n-1):
        indexkecil = cariposisiterkecil(A,i,n)
        if indexkecil != i:
            swap(A,i,indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));
