# 1.Girilen iki sayıyı toplayıp sonucunu ekrana yazdıran program?
# a = input ("Sayı Gir:")
# b = input ("Sayı Gir:")
# c = float(a)+float(b)
# print("Toplamları:", c)


# 2.V=I*R formülünü kullanarak verilen I ve R değerine göre V yi hesaplayan prog?
# I = input("Bir sayı giriniz:")
# R = input("Bir sayı giriniz:")
# V = float(I) * float(R)
# print("Çarpımları:", V)


# 3.Kısa ve uzun kenarı girilen dikdörtgenin alanını ve çevresini  hesaplayan prog?
# a = input("Uzun kenarı giriniz:")
# b = input("Kısa kenarı giriniz:")
# c = float(a) * float(b)
# d = 2*(float(a) + float(b))
# print("Dikdörtgenin alanı:", c)
# print("Dikdörtgenin çevresi:", d)


# 4.Yarıçapı verilen çemberin alanını hesaplayan prog (pi = 3,14)?
# a = input("Yarıçapı giriniz:")
# b = float(a) * float(a) * 3.14
# print("Alan(pi = 3,14):", b)


# 5.Girilen gün sayısını kaç yıl ve kaç ay olduğunu bulan program?
# a = input("Gün sayısını girin:")
# b = float(a)/365
# c = float(a)/30
# print("Yıl sayısı:", b)
# print("Ay sayısı(1 ay = 30 gün):", c)


# 6.100'lük sistemde notu girilen öğrencinin notunu 5'lik sisteme çeviriniz?
# a = input("Notunuzu giriniz:")
# b = float(a) * 5/100
# print("5'lik sistemde notunuz:", b)


# 7.Fiyat ve kdv oranı girilen ürünün toplam fiyatını ekrana yazdıran program?
# a = input("Ürünün fiyatını girin:")
# b = input("Üründe yüzde kaç kdv olduğunu giriniz:")
# d = float(a) * float(b)/100
# c = float(a) + float(d)
# print("Toplam fiyat:", c)


# 8.Bir ürünün alış fiyatı, vergi ve kar oranlarını kullanılarak satış fiyatını hesaplayan program?
# a = input("Alış fiyatını girin:")
# b = input("Üründe yüzde kaç vergi olduğunu girin:")
# c = input("Üründe yüzde kaç kar olduğunu girin:")
# d = float(a) * float(b)/100
# c = float(a) * float(c)/100
# e = float(d)+float(c)+float(a)
# print("Satış fiyatı:", e)


# 9.Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?
# a = input("3 Basamaklı sayı girin:")
# b = int(a[0]) * 100
# c = int(a[1]) * 10
# d = int(a[2])
# print("Yüzler basamağının değeri:", b)
# print("Onlar basamağının değeri:", c)
# print("Birler basamağının değeri:", d)


# 10.Klavyeden girilen 3 basamaklı sayının basamak değerlerini yazdıran program?
# a = input("3 Basamakli bir sayi girin:")
# e = a[2]+a[1]+a[0]
# print(e)


# 11.A ve B değişken değerlerini üçüncü bir değişken kullanmadan yer değiştiriniz?
# a = input("Yerlerinin değişmesini istediğiniz iki tane değişken girin:")
# b = a[1]+a[0]
# print(b)


# 12.Girilen n ve k değerlerine göre k + 2k + 3k + ...+nk yı hesaplayan program?  
# n = float(input("n değeri girin: "))
# k = float(input("k değeri girin: "))
# result = k * n * (n+1)/2
# print(result)


# 13.Çizginin başlangıç ve orta nokta koordinatları veriliyor. Diğer uç noktanın koordinatlarını bulunuz?
# basx = float(input("Çizginin başlangiç noktasinin apsisini girin:"))
# basy = float(input("Çizginin başlangiç noktasinin ordinatini girin:"))
# ortax = float(input("Çizginin orta noktasinin apsisini girin:"))
# ortay = float(input("Çizginin orta noktasinin ordinatini girin:"))
# sonx = (2 * ortax) - basx
# sony = (2 * ortay) - basy
# a = "Çizginin uç noktasinin kordinatlari: " + str(sonx) + "," + str(sony)
# print(a)
