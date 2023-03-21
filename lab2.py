import random
import math

#zad2
def lotto():
    tab = []
    y = len(tab)

    for i in range(6):
        i = random.randint(1,49)
        if i not in tab:
            tab.append(i)
    for x in tab:
        print(x)
lotto()

# #zad3
# def dodaj(x,y):
#     return x + y
# def odejmownie(x,y):
#     return x - y
# def mnozenie(x,y):
#     return x * y
# def dziel(x,y):
#     return x / y
# #zad4
# def obwKola(r):
#     return math.pi*2*r
# def polekola(r):
#     return math.pi*r*r
#
# print("Podaj liczbe pierwsza:")
# x = int(input())
# print("Podaj liczbe drugą:")
# y = int(input())
# print("Wybierz opcje wybierając 1 dla +, 2 dla -, 3 dla *, 4 dla / , 5 -> obw kola, 6 -> pole koła")
# w = int(input())
# if (w == 1):
#     print("suma: ", dodaj(x,y))
# elif (w == 2):
#     print("różnica: ", odejmownie(x,y))
# elif (w == 3):
#     print("mnożenie: ", mnozenie(x,y))
# elif (w == 4): print("dzielenie: ", dziel(x,y))
# elif (w == 5):
#     print("Podaj promien kola:")
#     r = int(input())
#     print("Obwód kola wynosi: ", obwKola(r))
# elif (w == 6):
#     print("Podaj promien kola:")
#     r = int(input())
#     print("Pole kola wynosi: ", polekola(r))
# else: print("Zly wybor")

#zad5
print("\n")
l = [3,4,5]
def sumaListy(l):
    s = 0
    for i in range(len(l)):
        s += l[i]
    return s
sumaListy(l)
def odczytaj(tab):
    for x in range(tab):
        print(x)
odczytaj(sumaListy(l))