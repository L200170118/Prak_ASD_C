class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def tinggiPohon(akar):
    if akar is None:
        return 0
    else :
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan:
            return kiri+1
        else :
            return kanan +1

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

print (tinggiPohon(A))
