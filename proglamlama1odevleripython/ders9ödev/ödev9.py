def BirinciCikti(sayi):
    for i in range(sayi):
        for j in range(sayi):
            print("*", end=" ")
        print()


def IkinciCikti(sayi):
    for i in range(1,sayi+1):
        print("*" * i, end=" ")
        print()


def UcuncuCikti(sayi):
    for i in range(1,sayi+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()


def DorduncuCikti(sayi):
    for i in range(1,sayi+1):
        print(str(i) * i)


def BesinciCikti(sayi):
    for i in range(sayi,0,-1):
        print(str(i) * i)
    for j in range(1,sayi+1):
        print(str(j) * j)


def AltinicCikti(sayi):
    a = 0
    for i in range(1,sayi+1):
        for j in range(1,i+1):
            a +=1
            print(a, end=" ")
        print()


def YedinciCikti(sayi):
    a = 0
    for i in range(1,sayi+1):
        for j in range(1,sayi+1):
            a +=1
            print(a, end=" ")
        print()
