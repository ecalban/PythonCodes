# 1.Aşağıdaki çıktıyı veren programı yazınız?
# def faktoriyel_hesabi(sayi):
#     carpim = 1
#     for s in range(1,sayi+1):
#         carpim = carpim * s
#     print(f"{sayi}! = {carpim}")
# for s in range(10):
#     faktoriyel_hesabi(s)


# sayının asal olup olmaması
# sayi = int(input("Sayı: "))
# def asal_hesabi(sayi):
#     kontrol = 0
#     for s in range(2,sayi):
#         if(sayi%s==0):
#             kontrol = 1
#             break
#     if(kontrol==0):
#         print(1)
#     else:
#         print(0)
# asal_hesabi(sayi)


# 2.İlk N asal sayısını listeleyen program?
# asal_list = []
# def asal_hesabi(sayi):
#     kontrol = 0
#     for s in range(2,sayi):
#         if(sayi%s==0):
#             kontrol = 1
#             break
#     if(kontrol==0):
#         asal_list.append(sayi)
# i = 2
# while True:
#     asal_hesabi(i)
#     i +=1
#     if(len(asal_list)==5):
#         break
# print(asal_list)


# 3.Girilen sayının kaç faktöriyel olduğunu bulunuz (720=6!)
# sayi = int(input("Sayı: "))
# def tersten_faktoriyel(sayi):
#     s = 1
#     carpim = 1
#     i = 0
#     while True:
#       carpim = carpim * s
#       s +=1
#       i +=1
#       if(carpim==sayi):
#         print(str(i) + "!")
#         break
# tersten_faktoriyel(sayi)


# 4.Listede en fazla tekrar eden elemanı silen program?


# 5.
# x = int(input("x: "))
# def faktoriyel_hesabi(sayi):
#     carpim = 1
#     for s in range(2,sayi+1):
#         carpim = carpim * s
#     return carpim
# toplam = 0
# for s in range(2,10+1):
#     toplam = toplam + (x**s)/faktoriyel_hesabi(s)
# toplam = toplam + (x + 1)
# print(toplam)


# 6.Girilen sayının Güçlü (1! + 4! + 5!  = 1 + 24 + 120 = 145) olup olmadığını bulan program?
# sayi = int(input("Sayı: "))
# a = sayi
# def faktoriyel_hesabi(x):
#     fak = 1
#     for i in range(1,x+1):
#         fak = fak * i
#     return fak
# toplam = 0
# while sayi>0:
#     son_rakam = sayi%10
#     toplam = toplam + faktoriyel_hesabi(son_rakam)
#     sayi = sayi // 10
# if(toplam==a):
#     print("Sayı güçlü")
# else:
#     print("Sayı güçlü değil")


# 7.PASCAL üçgeninin n. satırını üretiniz?


# 8.n satırlı PASCAL üçgenini çıktı veren programı yazınız?



        

            

        