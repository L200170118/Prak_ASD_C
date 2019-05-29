class SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None

def ukuranPohon(akar):
    ukuran = 0
    if akar is not None:
        if akar.kiri is None and akar.kanan is None:
            ukuran += 1
        else :
            hasil = ukuranPohon(akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran

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

print (ukuranPohon(A))






