## 1 den 100 e kadar olan sayılardan aynı anda 3 ve 5 e tam bölünen sayıları alt alta yazdıran python kodunu yazınız.
def UceBeseBolunenler(sayi):
    liste = []
    for i in range(1,sayi+1):
        if(i%3==0 and i%5==0):
            liste.append(i)
    return liste


## Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.
def TekveCiftlerinToplami(sayi):
    tek_toplam = 0
    cift_toplam = 0
    for i in range(1,sayi+1):
        if(i%2==0):
            cift_toplam +=i
        else:
            tek_toplam +=i
    return "Tek toplam: " + str(tek_toplam) + " Çift toplam: " + str(cift_toplam)


## 20'ye kadar olan sayıları, 10'dan küçük ve 10'dan büyük şeklinde listeleyecek Python kodu nasıl olmalıdır?
def YarisindanKucuklerVeBuyukler(sayi):
    orta = sayi // 2
    kucukler_listesi = []
    buyukler_listesi = []
    for i in range(1,sayi + 1):
        if(i>orta):
            buyukler_listesi.append(i)
        elif(i<orta):
            kucukler_listesi.append(i)
    return "Büyükler: " + str(buyukler_listesi) + " Küçükler: " + str(kucukler_listesi)


##Kullanıcının girdiği parolada Türkçe karakterlerin olmaması
##gerekmektedir. Buna göre kullanıcının girdiği parolada Türkçe
##karakter varsa “Parolada Türkçe karakter kullanılamaz.”
##Türkçe karakter yoksa “Parolanız oluşturulmuştur.” ekrana yazdırınız.
def ParolaOlusturma(parola):
    turkce_karakterler = ["ü","ğ","ı","ş","ç","İ","Ü","Ğ","Ş","Ğ","Ç"]
    kontrol = 0
    for i in parola:
        if i in turkce_karakterler:
            kontrol = 1
    if(kontrol==0):
        return "Parolanız oluşturulmuştur"
    else:
        return "Parolada Türkçe karakter kullanılamaz."


## Bir while döngüsü kullanarak kullanıcının tahmin etmesi için rastgele bir sayı oyunu oluşturan programı kodlayınız.
def SayiTahmini(tahmin,sayi):
    random = sayi
    if(tahmin==sayi):
        print("Doğru bildiniz")
    elif(tahmin<sayi):
        print("Az söylediniz")
        tahmin = int(input("Tahmininiz: "))
        SayiTahmini(tahmin,random)
    else:
        print("Çok söylediniz")
        tahmin = int(input("Tahmininiz: "))
        SayiTahmini(tahmin,random)
def RandomOlusturma():
    import random
    return round(random.random()*100)

    
## Kullanıcıdan alınan 5 sayı içerisinden for döngüsü kullanarak en küçük sayıyı bulan programı kodlayınız.
def EnKucuguBulma(dizi):
    min = dizi[0]
    for i in dizi:
        if(i<=min):
            min = i
    return min


#1 den 10′ a kadar sayıları tersten yani 10′ dan geriye yazdırın.
def TerstenYazdirma(sayi):
    for i in range(sayi,0,-1):
        print(i, end=" ")


## Kullanıcıdan isim ve soyisim bilgisini alan ve bunların harf uzunluğunu bulan programı yazınız. (Kullanıcıdan aldığınız değerleri bir diziye atayarak yapınız.)
def UzunlukBulma(isim,soyisim):
    isim_listesi = []
    soyisim_listesi = []
    for i in isim:
        isim_listesi.append(i)
    for j in soyisim:
        soyisim_listesi.append(j)
    return "İsim uzunluğu: " + str(len(isim_listesi)) + " Soyisim uzunluğu: " + str(len(soyisim_listesi))


## Bu listedeki üç sayıdan oluşan demetlerin (tuple) her birinin bir üçgen olup olmadığını ve hangi üçgen tipi olduğunu kontrol eden programı yazınız.
def UcgenKontrolu(a,b,c):
    import math
    if(abs(a-b)<c and abs(a+b)>c and abs(b-c)<a and abs(b+c)>a and abs(a-c)<b and abs(a+c)>b):
        if(a==b==c):
            return "Eşkenar üçgendir"
        elif(a==b or c==b or a==c):
            return "İkizkenar üçgen"
        else:
            return "Çeşitkenar"
    else:
        return "Üçgen değil"


## Aşağıdaki kurallara bağlı kalarak verilen gelir için gelir vergisini hesaplayın
## İlk 10.000$ 0
## Sonraki 10.000$ 10
## Kalan 20
## Örneğin, vergiye tabi gelirin 45000 olduğunu varsayarsak ve ödenecek gelir vergisi:
## 10000*0% + 10000*10% + 25000*20% = $6000
def VergiHesapla(gelir):
    if(gelir>20000):
        vergi = 10000*0 + 10000*0.1 + (gelir-20000)*0.2
        return "Verginiz: "  + str(vergi)
    elif(gelir>10000 and gelir<20000):
        vergi = 10000*0 + (gelir-10000)*0.1
        return "Verginiz: "  + str(vergi)
    else:
        return "Verginiz yok"
print(VergiHesapla(64000))

















