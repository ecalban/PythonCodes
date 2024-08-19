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
# standar_sapma = math.sqrt(toplam2/4)
# print(f"Standart sapma: {standar_sapma}")


# 3.Girilen sayının listede olup olmadığını bulan program?
# list = []
# eleman_sayisi = int(input("Listeniz kaç elemanlı: "))
# for e in range(eleman_sayisi):
#     object = input("Eleman girin: ")
#     list.append(object)
# object2 = int(input("Kontrol etmek istediğiniz sayı: "))
# if(str(object2) in list):
#     print("Girdiğiniz değer listede var")
# else:
#     print("Girdiğiniz değer listede yok")


# 4.Farklı değerlere sahip iki listenin korelasyon katsayısını hesaplayan program?


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
# eleman_sayisi = int(input("Listeniz kaç elemanlı: "))
# for x in range(eleman_sayisi):
#     object = int(input(f"Listenizin {x+1}. elemanı: "))
#     list.append(object)
# print("Listenizin küçükten büyüğe sıralanışı")
# list.sort()
# print(list)


# 6.Her elemanın tekrar sayısını bulan program?
# list = []
# eleman_sayisi = int(input("Listeniz kaç elemanlı: "))
# for x in range(eleman_sayisi):
#     object = input(f"Listenizin {x+1}. elemanı: ")
#     list.append(object)
# tekrar_eden_eleman = input("Ne kadar tekrar ettiğini öğrenmek istediğiniz eleman: ")
# if(tekrar_eden_eleman in list):
#     tekrar_sayisi = list.count(tekrar_eden_eleman)
#     print(f"Eleman listede {tekrar_sayisi} kere tekrar ediyor")
# else:
#     print("Seçtiğiniz eleman listede yok")


# 7.Girilen yazıdaki boşluk karakter sayısını bulan program?
# list = []
# string = str(input("Bir metin girin: "))
# list.extend(string)
# i = 0
# for l in list:
#     if(l==" "):
#         i +=1
#     else:
#         continue
# print(f"Yazınızdaki boşluk karakteri sayısı: {i}")


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











