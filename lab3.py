import random
import numpy

#zad 2
# tab = ["g","o","o","g","l","e"]
# print(tab[::-1])
# a = []
# n = int(input("Number of elements in array:"))
# for i in range(0,n):
#    l = str(input())
#    a.append(l)
# print(a)
# print(a[::-1])

#zad 3

def save_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(data + "\n")

b = []
n1 = random.randint(2,11)
for i in range(0,n1):
    los = random.randint(-5,5)
    b.append(los)
print(b)

# save_to_file("result.txt",data)

#zad 4
def kwad():
    tab2 = [[0 for x in range(5)] for y in range(5)]
    #print(tab2)
    # tab2[0] = [2,3,4,5,6]
    # print(tab2)
    for j in range(5):
        tab2[0][j] = j + 2
    for i in range(1,5):
        for j in range(5):
            tab2[i][j] = tab2[i-1][j]**2
    print(tab2)
print(kwad())

#zad5
# print(dict(a=1, b=2, c=3))
# print(dict([('d', 4), ('e', 5), ('f', 6)]))
# print(dict([('a', 1)], b=2, c=3))
# print(dict({'a': 1, 'b': 2}, c=3))
# tekst ="ala ma kota"
# for i in tekst:
#     dict

