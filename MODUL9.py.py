#Nama : Riris Agriela Savitri
#Nim  : L200170029
#Kelas: A

#nomer 5
class _SimpulPohonBiner(object):
    def __init__(self, data):
        self.data = data
        self.kiri = None
        self.kanan = None
   
A = _SimpulPohonBiner(14)
B = _SimpulPohonBiner(78)
C = _SimpulPohonBiner(39)
D = _SimpulPohonBiner(52)
E = _SimpulPohonBiner(83)
F = _SimpulPohonBiner(17)
G = _SimpulPohonBiner(9)
H = _SimpulPohonBiner(41)
I = _SimpulPohonBiner(2)
J = _SimpulPohonBiner(60)
K = _SimpulPohonBiner(23)
L = _SimpulPohonBiner(4)
M = _SimpulPohonBiner(19)

A.kiri = B; A.kanan = I
B.kiri = C; B.kanan = D
D.kiri = E; D.kanan = H
E.kiri = F; E.kanan = G
I.kiri = J; I.kanan = K
K.kiri = L; K.kanan = M

def preorderTrav(subpohon):
    if subpohon is not None:
        print(subpohon.data)
        preorderTrav(subpohon.kiri)
        preorderTrav(subpohon.kanan)

def inorderTrav(subpohon):
    if subpohon is not None:
        inorderTrav(subpohon.kiri)
        print(subpohon.data)
        inorderTrav(subpohon.kanan)

def postorderTrav(subpohon):
    if subpohon is not None:
        postorderTrav(subpohon.kiri)
        postorderTrav(subpohon.kanan)
        print(subpohon.data)

#nomer 6
##class SimpulPohonBiner(object):
##    def __init__(self, data):
##        self.data = data
##        self.kiri = None
##        self.kanan = None
##   
##
##A = SimpulPohonBiner("Ambarawa")
##B = SimpulPohonBiner("Bantul")
##C = SimpulPohonBiner("Cimahi")
##D = SimpulPohonBiner("Denpasar")
##E = SimpulPohonBiner("Enrekang")
##F = SimpulPohonBiner("Flores")
##G = SimpulPohonBiner("Garut")
##H = SimpulPohonBiner("Halmahera Timur")
##I = SimpulPohonBiner("Indramayu")
##J = SimpulPohonBiner("Jakarta")
##
##A.kiri = B; A.kanan = C
##B.kiri = D; B.kanan = E
##C.kiri = F; C.kanan = G
##E.kiri = H
##G.kanan = I

def ukuranPohon(akar):
    ukuran = 0
    if akar is not None:
        if akar.kiri is None and akar.kanan is None:
            ukuran +=1
        else:
            hasil = ukuranPohon(akar.kiri)
            ukuran += hasil
            hasil = ukuranPohon(akar.kanan)
            ukuran += hasil
    return ukuran

#nomer 7
def tinggiPohon(akar):
    if akar is None:
        return 0
    else:
        kiri = tinggiPohon(akar.kiri)
        kanan = tinggiPohon(akar.kanan)
        if kiri > kanan :
            return kiri +1
        else:
            return kanan +1

#nomer 8
def cetakDataDanLevel(akar, level =-1):
    level += 1
    if akar is not None:
        print(akar.data, "Level", level)
        cetakDataDanLevel(akar.kiri,level)
        cetakDataDanLevel(akar.kanan,level)
    
