# 1.Girilen 5 sayının ortalamasını bulan program?
# list = []
# toplam = 0
# for x in range(5):
#     object = int(input("Sayı girin: "))
#     toplam = toplam + object
#     list.append(object)
# ortalama = toplam/5
# print(f"Girilen sayıların ortalamaları: {ortalama}")


# 2.Girilen 5 sayının standart sapmasını bulan program?
# import math
# list = []
# toplam = 0
# for x in range(5):
#     object = int(input("Sayı girin: "))
#     toplam = toplam + object
#     list.append(object)
# ortalama = toplam/5
# toplam2 = 0
# for l in list:
#     toplam2 = toplam2 + ((ortalama - int(l)) ** 2)
# standart_sapma = math.sqrt(toplam2/4)
# print(f"Standart sapma: {standart_sapma}")


# 3.Girilen sayının listede olup olmadığını bulan program?
# list = []
# eleman_sayisi = int(input("Listenizin eleman sayısı: "))
# for x in range(eleman_sayisi):
#     eleman = int(input(f"Listenizin {x+1}. elemanı: "))
#     list.append(eleman)
# sayi = int(input("Sayı: "))
# kontrol = 0
# for i in range(eleman_sayisi):
#     if(int(list[i]) == sayi):
#         kontrol = 1
#     else:
#         continue
# if(kontrol==0):
#     print("Girilen sayı listede yok")
# else:
#     print("Girilen sayı listede var")


# 4.Farklı değerlere sahip iki listenin korelasyon katsayısını hesaplayan program?
# x = [1,2,3,4,5,6,7]
# y = [9,8,10,12,11,13,14]
# topx = 0
# topy = 0
# topxy = 0
# topxx = 0
# topyy = 0
# for i in range(7):
#     topx += x[i]
#     topy += y[i]
#     topxy += x[i] * y[i]
#     topxx += x[i] ** 2
#     topyy += y[i] ** 2
# Ex = topx / 7
# Ey = topy / 7
# Exy = topxy / 7
# Exx = topxx / 7
# Eyy = topyy / 7
# ExEx = Ex ** 2
# EyEy = Ey ** 2
# pay = Exy - (Ex * Ey)
# payda = ((Exx - ExEx) ** 0.5) * ((Eyy - EyEy) ** 0.5)
# kk = pay/payda
# print(kk)


# Eleman sayısı ve eleman değerleri girilen listenin elemanlarının liste ortalamasına göre durumu
# list = []
# eleman_sayisi = int(input("Listenizin eleman sayısı: "))
# toplam = 0
# for x in range(eleman_sayisi):
#     eleman = int(input(f"Listenizin {x+1}. elemanı: "))
#     toplam = toplam + eleman
#     list.append(eleman)
# ortalama = toplam/eleman_sayisi
# print(f"Ortalama: {ortalama}")
# for l in list:
#     if(l>ortalama):
#         print(f"Listenizin {l} elemanı ortalamadan büyük")
#     elif(l<ortalama):
#         print(f"Listenizin {l} elemanı ortalamadan küçük")
#     else:
#         print(f"Listenizin {l} elemanı ortalamaya eşit")


# 5.Elemanları sıralayan program?
# list = []
# es = int(input("Listenizin eleman sayısı: "))
# for i in range(es):
#     eleman = int(input("Listenin " + str(i+1) + ". elemanı: "))
#     list.append(eleman)
# for j in range(es-1):
#     for i in range(es-1):
#         if(list[i] > list[i+1]):
#             a = list[i]
#             list[i] = list[i+1]
#             list[i+1] = a
# print(list)


# 6.Her elemanın tekrar sayısını bulan program?


# 7.Girilen yazıdaki boşluk karakter sayısını bulan program?
# liste = []
# yazi = str(input("Yazı: "))
# for i in yazi:
#     liste.append(i)
# print(liste)
# for j in list:



# 8.Girilen iki yazıyı karşılaştıran (eşit olup olmadığını bulan) program
# ilk_yazi = str(input("İlk metniniz: "))
# ikinci_yazi = str(input("İkinci metniniz: "))
# ilk_liste = []
# ilk_liste.extend(ilk_yazi)
# ikinci_liste = []
# ikinci_liste.extend(ikinci_yazi)
# lenght1 = len(ilk_liste)
# lenght2 = len(ikinci_liste)
# if(lenght1!=lenght2):
#     print("Yazılar birbirinden farklı.")
# else:
#     for l in range(lenght1):
#         if(ilk_liste[l]!=ikinci_liste[l]):
#             print("Yazılar birbirinden farklı.")
#             break
#         elif(l == lenght1 - 1 and ilk_liste[-1]==ikinci_liste[-1]):
#             print("Yazılar birbirinin aynısı.")
        

# 9.Girilen yazının büyük yazılıp yazılmadığını bulan program?
# metin = str(input("Metin girin: "))
# list1 = []
# list2 = []
# cap = metin.upper()
# list1.append(metin)
# list2.append(cap)
# for s in range(len(list1)):
#     if(list1[s]!=list2[s]):
#         print("Metin büyük yazılmamış")
#         break
#     elif(list1[s]==list1[-1] and list1[-1]==list2[-1]):
#         print("Metin büyük yazılmış")
#         break


# 10.Girilen yazının k. karakteriyle r. karakteri arasını kopyalayan programı yazınız?


# 16.Girilen onluk sayıyı ikili sayıya dönüştürünüz?
# ikilik_list = []
# onluk = int(input("Onluk: "))
# while onluk>0:
#     ikilik_list.append(onluk%2)
#     onluk = onluk // 2
# for s in range(len(ikilik_list),0,-1):
#     print(ikilik_list[s-1], end="")


# 17.Girilen onluk sayıyı onaltılık sayıya dönüştürünüz?



# 18.Girilen ikilik sayıyı onluk sayıya dönüştürünüz?
# ikilik_liste = []
# ikilik_sayi = int(input("İkilik: "))
# while ikilik_sayi>0:
#     sonrakam = ikilik_sayi % 10
#     ikilik_liste.append(sonrakam)
#     ikilik_sayi = ikilik_sayi // 10
# onluk = 0
# for s in range(len(ikilik_liste)):
#     onluk = onluk + ((2**s) * ikilik_liste[s])
# print(onluk)




 


