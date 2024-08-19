
## Sayının en büyük iki çarpanı
# # sayi = int(input("Sayı: "))
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


##
# sayi = int(input("Sayı: "))
# def SayiyaKadar(sabit,degisken,toplam):
#     if(degisken==sabit):
#         print(toplam)
#         return
#     toplam += degisken
#     SayiyaKadar(sabit,degisken+1,toplam)
# SayiyaKadar(sayi,0,0)


##
# sayi = int(input("Sayı: "))
# def SayiyaKadar(sabit,degisken,toplam):
#     if(degisken==sabit):
#         print(toplam)
#         return
#     toplam *= degisken
#     SayiyaKadar(sabit,degisken+1,toplam)
# SayiyaKadar(sayi,1,1)


##
# kontrol = 0
# sayi = int(input("Sayı: "))
# degisen = sayi - 1
# def AsalKontrol(sabit,degisken,kontrol):
#     if(sabit%degisken==0):
#         kontrol = 1
#     elif(degisken == 1 and kontrol == 0):
#         print("asal")
#         return
#     AsalKontrol(sabit,degisken-1,kontrol)
# print(AsalKontrol(sayi,degisen,0))


##


