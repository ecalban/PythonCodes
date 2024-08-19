##Listeyi Matrise Çevirme
def ListeyiMatriseCevir(m1):
    for i in range(len(m1)):
        print(m1[i])


## 11.*Satır ve Sütun Toplamı:*
def MatrisinSatirveSutunToplami(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    sutuntop = []
    for i in range(sutun_sayisi):
        toplam = 0
        for j in range(satir_sayisi):
            toplam += m1[j][i]
        sutuntop.append(toplam)
    print("Sütun toplamı: " + str(sutuntop))
    print()
    satirtop = []
    for i in range(satir_sayisi):
        toplam = 0
        for j in range(sutun_sayisi):
            toplam += m1[i][j]
        satirtop.append(toplam)
    print("Satır toplamı: " + str(satirtop))

    
## 12.*Matrisin Normu:*
def MatrisinNormu(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    norm = 0
    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            norm += m1[i][j]
    print("Matrisin normu: " + str(norm))


## 13.*Matrisin Sıfıra Eşit Olup Olmadığını Kontrol Etme:*
def MatrisinSifiraEsitKontrolu(m1):
    kontrol = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if(m1[i][j]!=0):
                kontrol = 1
    if(kontrol==1):
        print("Sıfıra eşit değil")
    else:
        print("Sıfıra eşit")

## 14.*Matris Elemanlarını Ters Çevirme:*

## 15.*Matrisin İki Satırını Değiştirme:*
def MatrisinSatiriniDegistir(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    satir1 = round(random.random()*satir_sayisi)
    satir2 = round(random.random()*satir_sayisi)
    a = m1[satir1]
    m1[satir1] = m1[satir2]
    m1[satir2] = a
    ListeyiMatriseCevir(m1)



## 16.*Matrisin İki Sütununu Değiştirme:*
def MatrisinSutunuDegistir(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    sutun1 = round(random.random()*sutun_sayisi)
    sutun2 = round(random.random()*sutun_sayisi)
    for i in range(satir_sayisi):
        a = m1[i][sutun1]
        m1[i][sutun1] = m1[i][sutun2]
        m1[i][sutun2] = a
    ListeyiMatriseCevir(m1)


## 17.*Matrisin İki Satırını Çarpma:*


## 18.*Matrisin İki Sütununu Çarpma:*


## 19.*Matrisin Belirli Bir Satırını Sıfırlama:*
def MatrisinSatirSifirlama(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    random_satir = round(random.random()*satir_sayisi)
    for i in range(sutun_sayisi):
        m1[random_satir][i] = 0
    ListeyiMatriseCevir(m1)


## 20.*Matrisin Belirli Bir Sütununu Sıfırlama:*
def MatrisinSutunSifirla(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    random_sutun = round(random.random()*sutun_sayisi)
    for i in range(satir_sayisi):
        m1[i][random_sutun] = 0
    ListeyiMatriseCevir(m1)


## 21.*Matrisin Satırlarını Sıralama:*

                











































































































