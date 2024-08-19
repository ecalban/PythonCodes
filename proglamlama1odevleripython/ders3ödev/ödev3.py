# for x in range(10):
#     print(x, end=" ")


# x = range(3, 20, 2)
# for n in x:
#   print(n)


# x = 0
# while x < 10:
#     print(x, end=" ")
#     x +=1


# 1.Aşağıdaki çıktıyı veren programı yazınız?
# print("Element      Value")
# i = 0
# y = 2
# while i<10:
#     print(str(i) + "            " + str(y))
#     y = y+2
#     i +=1


# 2.Girilen 5 sayının ortalamasını bulan program?
# toplam = 0
# for a in range(5):
#     sayi = int(input("sayi:"))
#     toplam = toplam + sayi
# ort = toplam/5
# print(ort)
# i = 0
# toplam = 0
## while i<5:
#     i = i + 1
#     sayi = int(input("sayi: "))
#     toplam = toplam + sayi
# ort = toplam/5
# print(ort)


# 3.Girilen 5 sayı içerisindeki minimum ve maksimum değerleri bulan program?
# n = int(input("Sayı: "))
# mak = n
# min = n
# for s in range(4):
#     x = int(input("Sayı: "))
#     if(x>=mak):
#         mak = x
#     elif(x<min):
#         min = x
# print(mak)
# print(min)


# 4.N’e kadar tek sayıları yazdıran program?
# n = int(input("kaça kadar: "))
# for a in range(1,n,2):
#     print(a)
## n = int(input("kaça kadar: "))
# i = 0
# while i<n:
#     i = i + 1
#     if(i%2==1):
#         print(i)


# 5.Girilen sayının tam bölenlerini bulan program?
# sayi = int(input("sayi: "))
# for a in range(1,(sayi + 1)):
#     if(sayi%a==0):
#         print(a)
# sayi = int(input("sayı: "))
# sayi1 = sayi + 1
# i = 0
# while i<sayi1:
#     i = i + 1
#     if(sayi%i==0):
#         print(i)


# 6.a üzeri b'yi açık hesaplayan program?
# a = int(input("a: "))
# b = int(input("b: "))
# result = a ** b
# print(result)
## a = int(input("a: "))
# b = int(input("b: "))
# carpma = 1
# for x in range(b):
#     carpma = carpma * a
# print(carpma)


# 7. n’e kadar ki tek sayıların toplamı, çift sayıların çarpımını hesaplayan program?
# n = int(input("n sayısı: "))
# toplam = 0
# carpim = 1
# for a in range(1,n+1,1):
#     if(a%2==1):
#         toplam = toplam + a
#     else: carpim = carpim * a
# print("toplam: " + str(toplam) + " çarpım: " + str(carpim))
## n = int(input("n: "))
# toplam = 0
# carpim = 1
# i = 1
# while i < n:
#     i = i + 1
#     if(i%2==1):
#         toplam = toplam + i
#     else: carpim = carpim * i
# print("toplam: " + str(toplam) + " çarpım: " + str(carpim)) 


# 8.Girilen sayının faktöriyelini hesaplayan program?
# fak = 1
# n = int(input("n sayısı: "))
# for a in range(n,0,-1):
#     fak = fak * a
# print(fak)
## n = int(input("n sayısı: "))
# fak = 1
# i = 1
# while i<=n:
#     fak = fak * i
#     i = i + 1
# print(fak)

 
# 9.Girilen n değerine göre Fibonacci serisinin ( 0 1 1 2 3 5 8 … ) ilk n terimini hesaplayınız?
# n = int(input("n sayısı: "))
# c = 0
# a = 0
# b = 1
# while c < n:
#     print(b, end=" ")
#     c = a + b
#     a = b
#     b = c



# 10.Girilen n adet sayı içerisinden pozitif, negatif ve sıfır sayısının kaçar adet tekrarlandığını bulan program?
# n = int(input("Sayı adeti: "))
# pozitif = 0
# negatif = 0
# sifir = 0
# for s in range(n):
#     x = int(input("Sayı: "))
#     if(x>0):
#         pozitif = pozitif + 1
#     elif(x<0):
#         negatif = negatif + 1
#     else:
#         sifir = sifir + 1
# print(f"pozitif sayısı: {pozitif} negatif sayısı: {negatif} sıfır sayısı: {sifir}")


# 11.Serinin ilk elemanı, toplam eleman sayısını ve artış değeri girildiğinde seri sonucunu hesaplayan program?
# toplam = 0
# ilk = int(input("İlk eleman: "))
# eleman_sayisi = int(input("Eleman sayısı: "))
# artis = int(input("Artış miktarı: "))
# for s in range(eleman_sayisi):
#     toplam = toplam + ilk
#     ilk = ilk + artis
# print(toplam)


# 12.y = ax^2 + bx + c fonksiyonunun köklerini bulunuz?
# a = int(input("a değeri(ax^2 + bx + c): " ))
# b = int(input("b değeri(ax^2 + bx + c): " ))
# c = int(input("c değeri(ax^2 + bx + c): " ))
# delta = (b ** 2) - 4 * a * c 
# if delta<0:
#     print("kök yok")
# elif delta == 0:
#     x1 = (-b - (delta ** 0.5))/2 * a
#     print("çakışık iki kök: " + str(x1))
# else:
#     x1 = (-b - (delta ** 0.5))/2 * a
#     x2 = (-b + (delta ** 0.5))/2 * a
#     print("ilk kök: " + str(x1) + " ikinci kök: " + str(x2))


# 13.Girilen bir sayının asal olup olmadığını bulunuz?
# kontrol = 0
# sayi = int(input("Sayı: "))
# for s in range (2,sayi):
#     if(sayi%s==0):
#         kontrol = 1
# if(kontrol==0):
#     print("asal")
# else:
#     print("asal değil")


# 14.Girilen bir sayının asal çarpanlarını bulan program?


# 15.Girilen sayının basamak değerleri çarpımını bulunuz?
# sayi = int(input("Sayı: "))
# carpim = 1
# while sayi>0:
#     sonrakam = sayi%10
#     carpim = carpim * sonrakam
#     sayi = sayi // 10
# print(carpim)


# 16.Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?
# k = int(input("k: "))
# sayi = int(input("Sayı: "))
# while sayi>0:
#     sonrakam = sayi % 10
#     sayi = sayi // 10
#     if(sonrakam != k):
#         print(sonrakam, end=" ")
#     else:
#         continue
 

# 17.Girilen sayının basamak sayısını ekrana yazdıran program?
# i = 0
# sayi = int(input("Sayı: "))
# while sayi>0:
#     sonrakam = sayi % 10
#     i +=1
#     sayi = sayi // 10
# print(i)


# 18.TC kimlik noyu doğru girmeye zorlayınız? (11 karakter ve tamamı sayı)
# rakamlar = ["0","1", "2", "3", "4", "5", "6", "7", "8", "9"]
# tc = input("TC: ")
# i = 0
# for s in tc:
#     i +=1
# if(i!=11):
#     print("Hatalı giriş")
# else:
#     kontrol = 0
#     for x in tc:
#         if x not in rakamlar:
#             kontrol = 1
#             break
#         else:
#             continue    
#     if(kontrol==0):
#         print("Hatasız giriş")
#     else:
#         print("Hatalı giriş")


# 19.Girilen cümleyi tersten yazdırın? 
# a = input("cümle: ")
# cumle = a[::-1]
# for a in cumle:
#     print(a, end="")
## cumle = input(“Cümle=”)    
# tk = len(cumle)                   
# for i in range(tk-1,-1,-1):
#       print(cumle[i],end=””)


# 20.Girilen cümledeki sesli ve sessiz harf sayısını bulun?
# cumle = str(input("cumle: "))
# k = 0
# m = 0
# for x in cumle:
#     if(x==" " or x=="." or x==","):
#         continue
#     elif(x=="e" or x=="a" or x=="ö" or x=="o" or x=="ı" or x=="i" or x=="u" or x=="ü"):
#         k = k + 1
#     else:
#         m = m + 1
# print("sesli harf sayısı: " + str(k))
# print("sessiz harf sayısı: " + str(m))


# 21.Girilen cümledeki harflerin adetlerini ekrana yazın?
# cumle = str(input("cümle: "))
# i = 0
# for x in cumle:
#     if(x=="." or x=="," or x=="'" or x=="!" or x==" "):
#         continue
#     else:
#         i = i + 1
# print("harf sayısı: " + str(i))
## hs=0  # harf sayısı
# for chr in yazi:     
# 	if (ASCII(chr)>=97 and ASCII(chr)<=122) or (ASCII(chr)>=65 and ASCII(chr)<=90):
#                 hs+=1


# 22.Girilen sayının Pronic (ardışık iki sayının çarpımına eşit) olup olmadığını bulunuz?
# sayi = int(input("Sayı: "))
# kontrol = 0
# for s in range(sayi):
#     if(s * (s+1) == sayi):
#         kontrol = 1
#         break
# if(kontrol==0):
#     print("Pronic değil")
# else:
#     print("pronic")


# 23.N’e kadar ki Harshad (sayının kendisi rakamları toplamına bölünüyor) olanları listele


# 24.Girilen sayının Jumbled (komşu rakamlar arasındaki fark maksimum 1) olup olmadığını bulunuz?
# x = int(input(“x=”)) 
# a=x%
# while x>0:
# 	sonhane = x%10
#         if abs(sonhane-a)>1
# 		kontrol=1
# 		break
#         a = sonhane 
# 	x= x//10
# if kontrol ==1
# 	print(“jumled değil”)
# else
# 	print(“jumled”)


# 25.Girilen iki sayının OKEK (ortak katların en küçüğü) hesaplayan program?
# ilk_sayi = int(input("İlk sayı: "))
# ikinci_sayi = int(input("İkinci sayı: "))
# i = 0
# while True:
#     i +=1
#     if(i%ilk_sayi==0 and i%ikinci_sayi==0):
#         print(f"Ekok: {i}")
#         break


# 26.Girilen iki sayının OBEB (ortak bölenlerin en büyüğü) hesaplayan program?
# sayi1 = int(input("İlk sayı: "))
# sayi2 = int(input("İkinci sayı: "))
# if(sayi1>sayi2):
#     for x in range(sayi2,0,-1):
#         if(sayi1%x!=0 or sayi2%x!=0):
#             continue
#         elif(sayi1%x==0 and sayi2%x==0):
#             print("EBOB: " + str(x))
#             break
#         elif(x==1):
#             print("EBOB: 1")
# elif(sayi2>sayi1):
#     for x in range(sayi1,0,-1):
#         if(sayi1%x!=0 or sayi2%x!=0):
#             continue
#         elif(sayi1%x==0 and sayi2%x==0):
#             print("EBOB: " + str(x))
#             break
#         elif(x==1):
#             print("EBOB: 1")
# else:
#     print("EBOB: " + str(sayi2))


# 27.Sayı tahmin oyunu


# 28.Harf tahmin oyunu


# 29.Bir top X metre yükseklikten bırakılıyor. Her sıçrayışta  önceki yüksekliğini %20 kaybediyor. 1 metreden daha az olana kadar aldığı toplam yolu ve sıçrama sayısını hesaplayınız?
# yukseklik = int(input("X yüksekliği(metre): ")) 
# sicrama_sayisi = 0
# aldigi_yol = 0
# while True:
#     sicrama_sayisi = sicrama_sayisi + 1
#     aldigi_yol = aldigi_yol + (2 * yukseklik)
#     yukseklik = yukseklik - yukseklik/5
#     if (yukseklik<1):
#         print("Sıçrama sayısı: " + str(sicrama_sayisi) + " Aldığı toplam yol: " + str(aldigi_yol))
#         break
## x = int(input(“x=”))
# top=x
# s = 0
# while x>1
# x = x*0.8
# top+=2*x
# s+=1
# print(top,s)



# 30.Klavyeden 3 adet kenar uzunluğu giriliyor. Girilen kenar uzunlukları göz önüne alındığında üçgenin çizilip çizilemeyeceğini, çizilebilir ise türünü (ikizkenar, çeşitkenar, eşkenar), alanını ve çevresini hesaplayan program?
# import math
# kenar1 = int(input("İlk kenar: "))
# kenar2 = int(input("İkinci kenar: "))
# kenar3 = int(input("Üçüncü kenar: "))
# if(kenar1<=0 or kenar1<=0 or kenar1<=0):
#     print("Hatali giriş")
# elif(abs(kenar3 - kenar2)<kenar1 and kenar1<kenar3 + kenar2 and abs(kenar2 - kenar1)<kenar3 and kenar3<kenar1 + kenar2 and abs(kenar3 - kenar1)<kenar2 and kenar2<kenar3 + kenar1):
#     cevre = kenar1 + kenar2 + kenar3
#     alan = math.sqrt(cevre * ((cevre-kenar1) * (cevre-kenar2) * (cevre-kenar3)))
#     if(kenar1==kenar2==kenar3):
#         print("eşkenar üçgen ve alanı: " + str(alan) + " çevresi: " + str(cevre))
#     elif(kenar1==kenar2 or kenar3==kenar2 or kenar1==kenar3):
#         print("eşkenar üçgen ve alanı: " + str(alan) + " çevresi: " + str(cevre))
#     else:
#         print("çeşitkenar üçgen ve alanı: " + str(alan) + " çevresi: " + str(cevre))
# else:
#     print("üçgen çizilemez")  


# 31.Girilen sayının basamak değerlerinde k rakamı olmayanları listeleyen program?
# sayi = str(input("sayi: "))
# k = int(input("k sayısı: "))
# for x in sayi:
#     if(int(x)==k):
#         continue
#     else:
#         print(x, end=" ")
# # a = int(input(“a=”))
# k = int(input(“k=”))
# while a>0:
# son = a % 10
# if son!=k:
# print(son)
# a = a // 10


# 32.1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
# x = 1
# while x<=100:
#     x = x + 1
#     if(x%3==0 and x%5==0):
#         print(x)


# 33.Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
# sayi = int(input("Sayı: "))
# toplam_cift = 0
# toplam_tek = 0
# for s in range(sayi+1):
#     if(s%2==0):
#         toplam_cift = toplam_cift + s
#     else:
#         toplam_tek = toplam_tek + s
# print(f"Çiftlerin toplamı: {toplam_cift}, Teklerin toplamı: {toplam_tek}")


# 34.20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklinde listeleyecek Python kodu nasıl olmalıdır?
# print("10'dan küçük sayılar                       10'dan büyük sayılar(20'ye kadar)")
# for s in range(10):
#     print(s,"                                        ",s+11)
    

# 35.Kullanıcının girdiği parolada Türkçe karakterlerin olmaması gerekmektedir. Buna göre kullanıcının girdiği parolada Türkçe karakter varsa “Parolada Türkçe karakter kullanılamaz.” Türkçe karakter yoksa “Parolanız oluşturulmuştur.” ekrana yazdırınız


# 36.Bir while döngüsü kullanarak kullanıcının tahmin etmesi için rastgele bir sayı oyunu oluşturan programı kodlayınız.
# import random
# sayi = int(input("1-100 arası sayı girin: "))
# random = random.randint(1,100)
# while True:
#     if(sayi==random):
#         print("Doğru tahmin")
#     else:
#         print("Yanlış tahmin")
#         input("1-100 arası sayı girin: ")


# 37.Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.
# ilk_sayi = int(input("İlk sayı: "))
# ikinci_sayi = int(input("İkinci sayı: "))
# ucuncu_sayi = int(input("Üçüncü sayı: "))
# dorduncu_sayi = int(input("Dördüncü sayı: "))
# besinci_sayi = int(input("Beşinci sayı: "))
# buyuk_olan = 0
# list = []
# list.append(ilk_sayi)
# list.append(ikinci_sayi)
# list.append(ucuncu_sayi)
# list.append(dorduncu_sayi)
# list.append(besinci_sayi)
# for s in list:
#     if(int(s)>buyuk_olan):
#         buyuk_olan = s
# print(f"En büyük olanı: {buyuk_olan}")


# 38.Bir for döngüsü kullanarak Fibonacci dizisinin ilk 20 terimini hesaplayan bir Python programı nasıl yazılır?
# i = 0
# a = 1
# for x in range(20):
#     print(i, end=" ")
#     b = i + a
#     i = a
#     a = b


# 39.1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.
# for s in range(10,0,-1):
#     print(s, end=" ")


# 40.Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız. (Kullanıcıdan aldığınız değerleri bir diziye atayarak yapınız.)
# isim = str(input("İsim: "))
# soyisim = str(input("Soyisim: "))
# isim_listesi = []
# soyisim_listesi = [] 
# for s in isim:
#     isim_listesi.append(s)
# for i in soyisim:
#     soyisim_listesi.append(i)
# print(f"İsim uzunluğu: {len(isim_listesi)} Soyisim uzunluğu: {len(soyisim_listesi)}")


# 41.Bu listedeki üç sayıdan oluşan demetlerin (tuple) her birinin bir üçgen olup olmadığını ve hangi üçgen tipi olduğunu kontrol eden programı yazınız.
# edges = [(3, 4, 5), (5, 12, 13), (2, 15, 17), (5, 5, 5), (5, 5, 8), (1, 24, 25)]


# 42.kullanıcıdan öğrenci adını ve üç sınav notunu girmesini isteyin. Kullanıcı 'q' tuşuna basana kadar bu işlemi tekrarlansın. Ardından, öğrenci not bilgilerini ekrana yazdırın, her öğrencinin adını, notlarını ve ortalama notunu gösteren programı yazınız.


# 43.kullanıcıdan alınan n değerine kadar olan asal sayılar
# sayi = int(input("Sayı: "))
# if(sayi<=1):
#    print("Hatalı giriş")
# else:
#    for x in range(2,sayi+1):
#     for s in range(2,x+1):
#      if(s==x):
#         print(s)
#      elif(x%s!=0):
#         continue
#      elif(x%s==0):
#         break












