# 1.Girilen sayının pozitif ya da negatif olduğunu ekrana yazınız?
# a = float(input("Sayi:"))
# if(a>0):
#     print("Sayi pozitif")
# elif(a<0):
#     print("Sayi negatif")


# 2.Girilen tamsayının sıfır, pozitif ya da negatif olup olmadığını bulan program?
# a = int(input("Tamsayi girin:"))
# if(a>0):
#     print("Sayi pozitif")
# elif(a<0):
#     print("Sayi negatif")
# elif(a == 0):
#     print("Sayi 0")


# 3.Vize ve Final notu girilen öğrencinin geçip geçmediğini hesaplayan program (vizenin %40,finalin %60’ı hesaplanır. Final en az 55, ortalama en az 50 olunca geçer. Diğer durumlarda kalır)
# vize = float(input("Vize notunuz: "))
# final = float(input("Final notunuz: "))
# if(final>55):
#     ort = (final * 0.6) + (vize * 0.4)
#     if(ort>50):
#         print("Geçtiniz")
#     else: print("Kaldiniz:")
# else: print("Kaldiniz")


# 4.Kullanıcının girdiği üç sayıdan büyük olanını yazdıran program? 
# a = float(input("Sayi1: "))
# b = float(input("Sayi2: "))
# c = float(input("Sayi3: "))
# if(a>b and a>c):
#     print(a)
# elif(c>b and c>a):
#     print(c)
# elif(b>c and b>a):
#     print(b)


# 5.Girilen sayının 6'nın katı olduğunu bulan program?
# a = float(input("Sayi girin:"))
# b = a/6 - a//6
# if(b==0):
#     print("Sayi 6'nin kati")
# else: print("Sayi 6'nin kati degil")


# 6.Yüzlük notu harf notuna çeviriniz?
# a = float(input("Notunuzu girin:"))
# if(a>=90):
#     if(a<=100):
#         print("AA")
# elif(a>=85):
#     if(a<=89):
#         print("BA")
# elif(a>=80):
#     if(a<=84):
#         print("BB")
# elif(a>=75):
#     if(a<=79):
#         print("CB")
# elif(a>=70):
#     if(a<=74):
#         print("CC")
# elif(a>=60):
#     if(a<=69):
#         print("DC")
# elif(a>=50):
#     if(a<=59):
#         print("DD")
# elif(a>=0):
#     if(a<=49):
#         print("F")
# else: print("Hatali giriş")


# 7.İşçi maaşı ve çocuk sayısı verilmektedir. Çocuk sayısı bir ise %5, iki ise %10, üç veya daha fazla ise %15 zam yaparak yeni maaşı hesaplayınız?
# payment = float(input("Maaş girin: "))
# kid = float(input("Çocuk sayisini girin: "))
# if(kid==1):
#     newpayment = payment + (payment * 0.05)
#     print(newpayment)
# if(kid==2):
#     newpayment = payment + (payment * 0.10)
#     print(newpayment)
# if(kid>=3):
#     newpayment = payment + (payment * 0.15)
#     print(newpayment)
# else: print("Zam yok")


# 8.Ekrana 1:Toplama, 2:Çıkarma,..yaz. Sonra kullanıcıdan iki sayı alıp işlemi seçerek sonucu ekranda yazan program?
# sayi1 = float(input("Sayi1:"))
# sayi2 = float(input("Sayi2:"))
# islem = input("İşlem seçin:")
# if(islem=="Toplama"):
#     result = sayi1 + sayi2
#     print(result)
# if(islem=="Çıkarma"):
#     result = sayi1 - sayi2
#     print(result)
# if(islem=="Çarpma"):
#     result = sayi1 * sayi2
#     print(result)
# if(islem=="Bölme"):
#     result = sayi1 / sayi2
#     print(result)


# 9.Doğru daireyi kesiyor mu, kesmiyor mu, teğet mi sonucunu bulan program? 
# dogru: ax+by+c=0 
# daire: (x1,y1,r)
# import math
# a = float(input("Doğrunun a değerini girin(ax+by+c=0): "))
# b = float(input("Doğrunun b değerini girin(ax+by+c=0): "))
# c = float(input("Doğrunun c değerini girin(ax+by+c=0): "))
# x1 = float(input("Çembere merkez noktasinin apsis değerini girin: "))
# y1 = float(input("Çembere merkez noktasinin ordinat değerini girin: "))
# r = float(input("Çembere yariçap değerini girin: "))
# d = abs((a * x1) + (b * y1) + c) / math.sqrt((a ** 2) + (b ** 2))
# if(d==r):
#     print("Doğru çembere teğet")
# elif(d>r):
#     print("Doğru çemberi kesmez")
# elif(d<r):
#     print("Doğru çemberi keser")


# 10.A(x1,y2), B(x2,y2), C(x3,y3) üçgene ait üç nokta olduğuna göre P(xp,yp) üçgenin içinde mi dışında mı bulan program?










