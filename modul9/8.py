class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def cetakDataLevel(akar, level = -1):
    level +=1
    if akar is not None:
        print (akar.data, "Level", level)
        cetakDataLevel (akar.kiri,level)
        cetakDataLevel (akar.kanan,level)

A = SimpulPohonBiner('Ambarawa')
B = SimpulPohonBiner('Bantul')
C = SimpulPohonBiner('Cimahi')
D = SimpulPohonBiner('Denpasar')
E = SimpulPohonBiner('Enrekang')
F = SimpulPohonBiner('Flores')
G = SimpulPohonBiner('Garut')
H = SimpulPohonBiner('Halmahera Timur')
I = SimpulPohonBiner('Indramayu')
J = SimpulPohonBiner('Jakarta')

A.kiri = B; A.kanan = C
B.kiri = D; B.kanan = E
C.kiri = F; C.kanan = G
E.kiri = H
G.kanan = I

print (cetakDataLevel(A))

