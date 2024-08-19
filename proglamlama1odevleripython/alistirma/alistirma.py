## Kullanıcının girdiği parolada Türkçe karakterlerin olmaması gerekmektedir. Buna göre kullanıcının girdiği parolada Türkçe karakter varsa “Parolada Türkçe karakter kullanılamaz.” Türkçe karakter yoksa “Parolanız oluşturulmuştur.” ekrana
# turkce = ["ü","ğ","ö","ı","İ","ş"]
# parola = input("Parola: ")
# for i in parola:
#     kontrol = 0
#     if(str(i) in turkce):
#         kontrol = 1
#         break
# if(kontrol==0):
#     print("Parolanız oluşturuldu")
# else:
#     print("Parolada Türkçe karakter kullanılamaz.")


## Bir while döngüsü kullanarak kullanıcının tahmin etmesi için rastgele bir sayı oyunu oluşturan programı kodlayınız.
# sayi = int(input("Tahmininiz: "))
# import random
# rastgele = random.randint(1,100)
# while sayi!=rastgele:
#     sayi = int(input("Tahmininiz: "))
# print("Doğru tahmin")


## Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.
# liste = []
# for i in range(5):
#     eleman = int(input("Sayı: "))
#     liste.append(eleman)
# min = liste[0]
# for i in liste:
#     if(i<=min):
#         min = i
# print(min)
    

## Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız. (Kullanıcıdan aldığınız değerleri bir diziye atayarak yapınız.)
# isim = input(str("İsim: "))
# soyisim = input(str("Soyisim: "))
# isim_list = []
# soyisim_list = []
# for i in isim:
#     isim_list.append(i)
# for x in soyisim:
#     soyisim_list.append(x)
# print("İsim uzunluğu: " + str(len(isim_list)) + " Soyisim uzunluğu: " + str(len(soyisim_list)))


## Kullanıcıdan öğrenci adını ve üç sınav notunu girmesini isteyin.  Kullanıcı 'q' tuşuna basana kadar bu işlemi tekrarlansın. Ardından, öğrenci not bilgilerini ekrana yazdırın, her öğrencinin adını, notlarını ve ortalama notunu gösteren programı yazınız.
# isim = str(input("İsim: "))
# not1 = int(input("Not 1: "))
# not2 = int(input("Not 2: "))
# not3 = int(input("Not 3: "))
# bilgi_listesi = []
# while True:
#     eleman = "İsim: " + isim + " - Not 1: " + str(not1) + " - Not 2: " + str(not2) + " - Not 3: " + str(not3) + " - Ortalama: " + str((not1+not2+not3)/3)
#     bilgi_listesi.append(eleman)
#     isim = str(input("İsim: "))
#     if(isim=="q"):
#         break
#     not1 = int(input("Not 1: "))
#     not2 = int(input("Not 2: "))
#     not3 = int(input("Not 3: "))
# for i in bilgi_listesi:
#     print(i)


## Fibonacci serisini 0 ile 50 arasında elde eden bir Python programı yazınız
# x = 0
# y = 1
# while x<=50:
#     print(x, end=" ")
#     z = x + y
#     x = y
#     y = z


# liste = []
# eleman = str(input("Eleman(q girerseniz liste sonlanır): "))
# while eleman != "q":
#     liste.append(int(eleman))
#     eleman = str(input("Eleman(q girerseniz liste sonlanır): "))
# sayi = int(input("Listede kontrol edilecek sayı: "))
# kontrol = 0
# for i in liste:
#     if(i==sayi):
#         kontrol = 1
# if(kontrol==0):
#     print("Girilen sayı listede yok")
# else: 
#     print("Girilen sayı listede var")


# liste = []
# eleman = str(input("Eleman(q girerseniz liste sonlanır): "))
# while eleman != "q":
#     liste.append(int(eleman))
#     eleman = str(input("Eleman(q girerseniz liste sonlanır): "))
# print(liste)
# for i in range(len(liste)-1):
#     for x in range(len(liste)-1):
#         if(liste[x]>liste[x+1]):
#             a = liste[x]
#             liste[x] = liste[x+1]
#             liste[x+1] = a
# print(liste)


# liste = []
# def asal_hesabi(x):
#     kontrol = 0
#     for i in range(2,x):
#         if(x%i==0):
#             kontrol = 1
#             break
#     if(kontrol==0):
#         liste.append(x)
# n = int(input("N: "))
# a = 2
# while True:
#     asal_hesabi(a)
#     a = a + 1
#     if(len(liste)==n):
#         break
# print(liste)



# def ParalellikKontolu(liste1,liste2):
#     if(liste1[0]/liste1[1]==liste2[0]/liste2[1]):
#         return "paraleldir"
#     else:
#         return "paralel değil"
# print(ParalellikKontolu([2,1,5],[6,3,9]))


## Palindrom ve Smith konrolü
# def Palindrom_kontrolu(sayi):
#     a = sayi
#     ters = ""
#     while sayi>0:
#         son_rakam = sayi%10
#         ters = ters + str(son_rakam)
#         sayi = sayi//10
#     if(ters == str(a)):
#         return True
#     else:
#         return False
# def Smith_kontrolu(sayi):
#     b = sayi
#     carpan_listesi = []
#     for i in range(2,sayi+1):
#         if(sayi%i==0):
#             carpan_listesi.append(i)
#     asal_carpan_listesi = []
#     for i in carpan_listesi:
#         kontrol = 0
#         for j in range(2,i):
#             if(i%j==0):
#                 kontrol = 1
#                 break
#         if(kontrol==0):
#             asal_carpan_listesi.append(i)
#     asal_carpanlarin_toplami = 0
#     for i in asal_carpan_listesi:
#         if(i>10):
#             while i>0:
#                 i_son_rakam = i%10
#                 asal_carpanlarin_toplami += i_son_rakam
#                 i = i//10
#         else:
#             asal_carpanlarin_toplami +=i
#     kendi_rakamlarinin_toplami = 0
#     while b>0:
#         b_son_rakam = b%10
#         kendi_rakamlarinin_toplami += b_son_rakam
#         b = b//10
#     if(kendi_rakamlarinin_toplami==asal_carpanlarin_toplami):
#         return True
#     else:
#         return False
# def Palindrom_Smith_Kontrolu(sayi):
#     if(Palindrom_kontrolu(sayi)==Smith_kontrolu(sayi) and Palindrom_kontrolu(sayi) == True):
#         return "Sayı Palindrom ve Smith"
#     elif(Palindrom_kontrolu(sayi)==Smith_kontrolu(sayi) and Palindrom_kontrolu(sayi) == False):
#         return "Sayı Palindrom da Smith de değildir"
#     elif(Palindrom_kontrolu(sayi)!=Smith_kontrolu(sayi) and Palindrom_kontrolu(sayi) == True):
#         return "Sayı Palindrom ama Smith değil"
#     elif(Palindrom_kontrolu(sayi)!=Smith_kontrolu(sayi) and Palindrom_kontrolu(sayi) == False):
#         return "Sayı Palindrom değil ama Smith"
# def main():
#     sayi = int(input("Kontrol edilecek sayı: "))
#     print(Palindrom_Smith_Kontrolu(sayi))
# main()


## Kuvvet asalı  sayısı kontrolü
# def KuvvetAsali(sayi):
#     asal_listesi = []
#     for i in range(2,sayi):
#         kontrol = 0
#         for j in range(2,i):
#             if(i%j==0):
#                 kontrol = 1
#         if(kontrol==0):
#             asal_listesi.append(i)
#     kontrol = 0
#     for i in range(len(asal_listesi)):
#         for j in range(len(asal_listesi)):
#             if(asal_listesi[i]**asal_listesi[j] + 2 == sayi):
#                 kontrol = 1
#                 break
#     if(kontrol == 1):
#         return "Kuvvet asalıdır"
#     else:
#         return "Kuvvet asalı değildir"


## Asalımsı sayı fonksiyonu
# def AsalımsıSayi(sayi):
#     carpan_listesi = []
#     for i in range(2,sayi+1):
#         if(sayi%i==0):
#             carpan_listesi.append(i)
#     asal_carpan_listesi = []
#     for i in carpan_listesi:
#         kontrol = 0
#         for j in range(2,i):
#             if(i%j==0):
#                 kontrol = 1
#         if(kontrol == 0):
#             asal_carpan_listesi.append(i)
#     carpim_listesi = []
#     for i in range(len(asal_carpan_listesi)):
#         for j in range(len(asal_carpan_listesi)):
#             carpim = 1
#             if(i!=j):
#                 carpim = asal_carpan_listesi[i] * asal_carpan_listesi[j]
#                 if carpim not in carpim_listesi:
#                     carpim_listesi.append(carpim)
#     toplam = 0
#     for i in carpim_listesi:
#         toplam +=i
#     kontrol = 0
#     for i in range(2,toplam):
#         if(toplam%i==0):
#             kontrol = 1
#             break
#     if(kontrol == 0):
#         return "Asalımsı sayıdır"
#     else:
#         return "Asalımsı sayı değildir"        


## Narsistik sayı kontrolü
# def NarsistikSayi(sayi):
#     a = sayi
#     b = sayi
#     basamak_sayisi = 0
#     while sayi>0:
#         son_rakam = sayi%10
#         basamak_sayisi +=1
#         sayi = sayi //10
#     toplam = 0
#     while a>0:
#         son_rakam = a%10
#         toplam += (son_rakam ** basamak_sayisi)
#         a = a // 10
#     if(toplam == b):
#         return "Narsistik sayıdır"
#     else:
#         return "Narsistik sayı değildir"


## Elemanları sıralayan program
# def ElemanSiralama(liste):
#     for i in range(len(liste)):
#         for i in range(len(liste)-1):
#             if(liste[i]>=liste[i+1]):
#                 a = liste[i]
#                 liste[i] = liste[i+1]
#                 liste[i+1] = a
#     return liste


## Boşluk sayısını bulma
# def YazidaBulma(yazi):
#     kelime_listesi = []
#     kelime = ""
#     for i in yazi: 
#         if i!=" ":
#             kelime +=i
#         else:
#             kelime_listesi.append(kelime)
#             kelime = ""
#     kelime_sayisi = len(kelime_listesi) + 1
#     rakamlar = ["0","1","2","3","4","5","6","7","8","9"]
#     rakam_sayisi = 0
#     for i in yazi:
#         if i in rakamlar:
#             rakam_sayisi +=1
#     karakter_sayisi = len(yazi)
#     return "Kelime sayısı: " + str(kelime_sayisi) + " Rakam sayısı: " + str(rakam_sayisi) + " Karakter sayısı: " + str(karakter_sayisi)


## Sayının en büyük iki çarpanı
# sayi = int(input("Sayı: "))
# a = sayi-1
# kontrol1 = 0
# def BuyukCarpanlariBulma(sabit,degisen,kontrol1):
#     if(sabit%degisen==0):
#         print(degisen)
#         BuyukCarpanlariBulma(sabit,degisen-1,kontrol1+1)
#     elif(kontrol1==2):
#         return
#     else:
#         BuyukCarpanlariBulma(sabit,degisen-1,kontrol1)
# print(BuyukCarpanlariBulma(sayi,a,kontrol1))


##
# x = int(input("X: "))
# n = int(input("N: "))
# degisen = x + 2
# def AlanYazma(sabit,degisken,kontrol):
#     if(kontrol==0):
#         return
#     print(sabit*degisken)
#     AlanYazma(sabit,degisken+2,kontrol-1)
# print(AlanYazma(x,degisen,n))


## Çalışma sorularında mitoz bölünme sorusu
# n = int(input("N: "))
# def Mitoz(sabit,kontrol):
#     if(kontrol==10):
#         return
#     yeni_hucreler = sabit * 2
#     oluden_sonra = yeni_hucreler - (yeni_hucreler * 0.2)
#     print(oluden_sonra)
#     Mitoz(oluden_sonra,kontrol+1)
# print(Mitoz(n,0))

## listede harf tekrarını özyinelemeli bulma
# def HarfTekrari(liste,harf):
#     sayi = 0
#     for i in liste:
#         if(i==harf):
#             sayi +=1
#     return sayi
# print(HarfTekrari(["i","a","e","i","a","i"],"i"))


## cumlede bosluk sayısını özyinelemeli bulma 
# def BoslukSayisi(cumle):
#     bosluk = 0
#     for i in cumle:
#         if(ord(i)==32):
#             bosluk +=1
#     return bosluk
# print(BoslukSayisi("Eren Çalban "))


## Kelime sayısını özyinelemeli bulma
# def KelimeSayisi(cumle):
#     kelime_listesi = []
#     kelime = ""
#     for i in cumle:
#         if(i != " "):
#             kelime +=i
#         kelime_listesi.append(kelime)
#         kelime = ""
#     return str(kelime_listesi) + " "  + str(len(kelime_listesi)+1)
# print(KelimeSayisi("Eren Çalban "))


## Büyük, küçük, rakam ve diğer karakterlerin sayısını bulma
# def BuyukKucukRakamDiger(cumle):
#     buyuk_harf_sayisi = 0
#     kucuk_harf_sayisi = 0
#     rakam_sayisi = 0
#     diger_sayisi = 0
#     for i in cumle:
#         if(ord(i)>64 and ord(i)<91):
#             buyuk_harf_sayisi +=1
#         elif(ord(i)>96 and ord(i)<123):
#             kucuk_harf_sayisi +=1
#         elif(ord(i)>47 and ord(i)<58):
#             rakam_sayisi +=1
#         else:
#             diger_sayisi +=1
#     a = {"Büyük harf sayısı: " + str(buyuk_harf_sayisi),
#          "Küçük harf sayısı: " + str(kucuk_harf_sayisi),
#          "Rakam sayısı: " + str(rakam_sayisi),
#          "Diğer karakterlerin sayısı: " + str(diger_sayisi)}
#     return a
# print(BuyukKucukRakamDiger("Eren Calban 564864 --.."))


## Kelimenin düz ve tersi aynı mı kontrol eden prog
# def KelimePalindrom(kelime):
#     kelime_listesi = []
#     for i in kelime:
#         kelime_listesi.append(i)
#     yeni_kelime = ""
#     for i in range(len(kelime_listesi)-1,-1,-1):
#         yeni_kelime +=kelime_listesi[i]
#     if(yeni_kelime == kelime):
#         return True
#     else:
#         return False
# print(KelimePalindrom("ErennerE"))


## listede indeks, elemanlar ve eleman kadar yıldız yazan prog
# def YildizYaz(liste):
#     for i in range(len(liste)):
#         print(str(i) + " " + str(liste[i]) + " " + "*"*(liste[i]))
# YildizYaz([1,5,6,8,2,3,5,7,1,5])


## listedeki çiftleri 1 arttırarak tek yapan prog
# def ListedeCiftiTek(liste):
#     for i in range(len(liste)):
#         if(liste[i]%2==0):
#             liste[i] = liste[i] + 1
#     return liste
# print(ListedeCiftiTek([2,5,6,8,9,5,2,4,5,60,40,70,52,51,64,80]))

      
## yanyana olan çiftleri yazdıran prog
# def YanYanaCiftler(liste):
#     for i in range(len(liste)-1):
#         if(liste[i]%2==0 and liste[i+1]%2==0):
#             print(str(liste[i]) + "-" + str(liste[i+1]), end=" ")
# print(YanYanaCiftler([1,3,4,8,6,5,3,8,2,5,6,4]))


## 1-100 arasında rastgele oluşan matriste 50 den büyükleri yazdıran prog
# def EllidenBuyuk():
#     import random
#     m1 = []
#     for i in range(3):
#         satir = []
#         for j in range(3):
#             satir.append(round(random.random()*100))
#         m1.append(satir)
#     for i in range(3):
#         print(m1[i])
#     buyuk_liste = []
#     for i in range(3):
#         for j in range(3):
#             if(m1[i][j]>50):
#                 buyuk_liste.append(m1[i][j])
#     print()
#     print(buyuk_liste)
# EllidenBuyuk()


## 1-100 arasında rastgele oluşan matriste max min ve ortalama bulan prog
# def MatristeBul():
#     import random
#     m1 = []
#     for i in range(4):
#         satir = []
#         for j in range(4):
#             satir.append(round(random.random()*100))
#         m1.append(satir)
#     for i in range(4):
#         print(m1[i])
#     mak = m1[0][0]
#     min = m1[0][0]
#     toplam = 0
#     for i in range(4):
#         for j in range(4):
#             toplam +=m1[i][j]
#             if(m1[i][j]>mak):
#                 mak = m1[i][j]
#             elif(m1[i][j]<min):
#                 min = m1[i][j]
#     ortalama = (toplam)/16
#     print("Maksimum: " + str(mak))
#     print("Minimum: " + str(min))
#     print("Ortalama: " + str(ortalama))
# MatristeBul()

##1 den 10 a olan sayıları ve karelerinin matrisi
# def Kareleriyle():
#     m1 = []
#     for i in range(10):
#         satir = [i+1,(i+1)**2]
#         m1.append(satir)
#     for i in range(10):
#         print(m1[i])
# Kareleriyle()
        
## matriste sol köşegen ve sağ köşegenin toplamları
# def KosegenToplamlari():
#     import random
#     m1 = []
#     kosegen1 = 0
#     kosegen2 = 0
#     for i in range(4):
#         satir = []
#         for j in range(4):
#             random1 = round(random.random()*10)
#             if(i==j):
#                 kosegen1+=random1
#             elif(i==3-j):
#                 kosegen2+=random1
#             satir.append(random1)
#         m1.append(satir)
#     for i in range(4):
#         print(m1[i])
#     print()
#     print(kosegen1)
#     print(kosegen2)
# KosegenToplamlari()


## 9 a kadar olan sayıların faktoriyelleri
# def fun():    
#     for i in range(10):
#         faktoriyel = 1
#         for j in range(1,i+1):
#             faktoriyel *=j
#         print(str(i) + "! = " + str(faktoriyel))
# fun()


## ilk n kadar asalı yazdır 
# def AsalListele(n):
#     asal_listesi = []
#     degisen = 2
#     while True:
#         kontrol = 0
#         for i in range(2,degisen):
#             if(degisen%i==0):
#                 kontrol = 1
#                 break
#         if(kontrol == 0):
#             asal_listesi.append(degisen)
#         if(len(asal_listesi)==n):
#             break
#         degisen +=1
#     return asal_listesi
# print(AsalListele(5))


## sayının kaç faktoriyel olduğunu bulan prog
# def Fak(sayi):
#     carpim = 1
#     for i in range(2,sayi):
#         carpim *=i
#         if(carpim==sayi):
#             return str(i) + "!"
# print(Fak(720)) 


## listede en fazla tekrar edeni silen prog
# def Sil(liste):
#     mak = 0
#     for i in liste:
#         es = 0
#         for j in liste:
#             if(i==j):
#                 es +=1
#         if(es>mak):
#             mak = es
#             mak_indeks = i
#     yeni_liste = []
#     for j in liste:
#         if(j!=mak_indeks):
#             yeni_liste.append(j)
#     return yeni_liste
# print(Sil([1,1,2,5,6,8,52,6,2,21,5,8,9,6,2,1,1]))


## sayının güçlü sayı(rakamlarının faktoriyelleri toplamı sayıya eşit) kontrolü
# def guclu(sayi):
#     c = sayi
#     toplam = 0
#     while sayi>0:
#         son_rakam = sayi%10
#         faktoriyel = 1
#         for i in range(2,son_rakam+1):
#             faktoriyel *=i
#         toplam +=faktoriyel
#         sayi = sayi // 10
#     if(toplam==c):
#         return True
#     else:
#         return False
# print(guclu(145))


## sayının mükemmel sayı(çarpanları toplamı sayıya eşit) kontrolü
# def Mukemmel(sayi):
#     carpan_toplam = 0
#     for i in range(1,sayi):
#         if(sayi%i==0):
#             carpan_toplam +=i
#     if(carpan_toplam==sayi):
#         return True
#     else:
#         return False
# print(Mukemmel(496))    


## Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz?
# def Pronic(sayi):
#     kontrol = 0
#     for i in range(sayi):
#         if(i*(i+1)==sayi):
#             kontrol = 1
#             break
#     if(kontrol==0):
#         return False
#     else:
#         return True
# print(Pronic(12))


## N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele? 
# def Harshad(sayi):
#     rakam_toplam = 0
#     c = sayi
#     while sayi>0:
#         son_rakam = sayi % 10
#         rakam_toplam +=son_rakam
#         sayi = sayi//10
#     if(c%rakam_toplam==0):
#         return True
#     else:
#         return False
# print(Harshad(150))



def BuyukKucukEsit(liste):
    for i in range(len(liste)):
        toplam = 0
        for j in range(i):
            toplam += liste[j]
        if(toplam==liste[i]):
            print("Listenin " + str(i) + ". indeksi kendinden öncekilerin toplamına eşit")
        elif(toplam<liste[i]):
            print("Listenin " + str(i) + ". indeksi kendinden öncekilerin toplamından büyük")
        else:
            print("Listenin " + str(i) + ". indeksi kendinden öncekilerin toplamından küçük")
BuyukKucukEsit([1,5,9,6,21,42,100,3])

        


##
