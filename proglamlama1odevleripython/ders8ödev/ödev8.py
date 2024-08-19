## Listeyi matris şeklinde yazdırma
def ListeyiMatriseCevir(m1):
    for i in range(len(m1)):
        print(m1[i])


## İki matrisin toplamını bul.
def MatrisToplama(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    m2 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m2.append(satir)
    ListeyiMatriseCevir(m2)
    print()
    m3 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(m1[i][j] + m2[i][j])
        m3.append(satir)
    ListeyiMatriseCevir(m3)
    print()


## Matrisin satır ve sütun toplamlarını hesapla.
def MatrisinSatirVeSutunToplami(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    sutun_listesi = []
    for i in range(sutun_sayisi):
        toplam = 0
        for j in range(satir_sayisi):
            toplam +=m1[j][i]
        sutun_listesi.append(toplam)
    print(sutun_listesi)
    print()
    satir_listesi = []
    for i in range(satir_sayisi):
        toplam = 0
        for j in range(sutun_sayisi):
            toplam +=m1[i][j]
        satir_listesi.append(toplam)
    print(satir_listesi)


## Matristeki en büyük sayıyı bul.
def MatristeEnBuyuk(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    mak = m1[0][0]
    for i in range(satir_sayisi):
        for j in range(sutun_sayisi):
            if(m1[i][j]>=mak):
                mak = m1[i][j]
    print("Maksimum: " + str(mak))


## Matris izini (diyagonal toplam) bul.
def MatrisiIzi(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    if(satir_sayisi==sutun_sayisi):
        toplam = 0
        for i in range(satir_sayisi):
            for j in range(sutun_sayisi):
                if(i==j):
                    toplam += m1[i][j]
        print("Diyagonal toplam : " + str(toplam))
    else:
        print("Matrisin izi bulunamaz")                


## Verilen sayıyı matrisin k. indeksine yerleştir
def MatriseYerlestir(satir_sayisi,sutun_sayisi,satir_indeks,sutun_indeks,sayi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    m1[satir_indeks][sutun_indeks] = sayi
    ListeyiMatriseCevir(m1)


## Matrisin transpozunu alın.
def MatrisinTranspozu(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    m2 = []
    for i in range(sutun_sayisi):
        satir = []
        for j in range(satir_sayisi):
            satir.append(m1[j][i])
        m2.append(satir)
    ListeyiMatriseCevir(m2)


## İki matrisin çarpımını hesaplayan prog?
def MatrisCarpimi(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    m2 = []
    for i in range(sutun_sayisi):
        satir = []
        for j in range(satir_sayisi):
            satir.append(round(random.random()*10))
        m2.append(satir)
    ListeyiMatriseCevir(m2)
    print()
    m3 = []
    for i in range(satir_sayisi):
        satir = []
        for j in range(satir_sayisi):
            satir.append(round(random.random()*10))
        m3.append(satir)
    for i in range(len(m1)):
        for j in range(len(m1)):
            m3[i][j] = 0
            for k in range(len(m1[0])):
                m3[i][j] += m1[i][k]*m2[k][j]
    ListeyiMatriseCevir(m3)



## Girilen N değerine göre NxN boyutlu bir matrisin hücrelerine 1 den NxN'e kadar sayıları yerleştir.
def NBoyutluMatris(n):
    a = 1
    m1 = []
    for i in range(n):
        satir = []
        for j in range(n):
            satir.append(a)
            a +=1
        m1.append(satir)
    ListeyiMatriseCevir(m1)


## 0-1 değerlerini içeren bir matristeki nesnenin alanını hesapla.
def MatrisinAlani(m1):
    alan = 0
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if(m1[i][j]==1):
                alan +=1
    return alan


## 0-1 değerlerini içeren bir matristeki nesnenin kenarlarını hesapla.
def MatrisinCevresi(m1):
    m2 = m1
    ListeyiMatriseCevir(m1)
    print()
    for i in range(1,len(m1)-1):
        for j in range(1,len(m1[0])-1):
            if(m1[i][j]==1 and m1[i][j+1]==1 and m1[i][j-1]==1 and m1[i+1][j]==1 and m1[i+1][j+1]==1 and m1[i+1][j-1]==1 and m1[i-1][j]==1 and m1[i-1][j+1]==1 and m1[i-1][j-1]==1):
                m2[i][j]=0
    ListeyiMatriseCevir(m2)



## Matristeki şekli n kat büyüten programı yazınız?


## Diyagonallerin yerini değiştir
def DiyagonallerinYeriniDegis(satir_sayisi,sutun_sayisi):
    import random
    m1 = []
    for i in range(satir_sayisi):
        satir = []
        for i in range(sutun_sayisi):
            satir.append(round(random.random()*10))
        m1.append(satir)
    ListeyiMatriseCevir(m1)
    print()
    if(satir_sayisi==sutun_sayisi):
        k = satir_sayisi - 1
        for i in range(satir_sayisi):
            for j in range(sutun_sayisi):
                if(i==j):
                    a = m1[i][j]
                    m1[i][j] = m1[i][k-j]
                    m1[i][k-j] = a
        ListeyiMatriseCevir(m1)
    else:
        print("Matrisin diyagonali yoktur")

                
    












