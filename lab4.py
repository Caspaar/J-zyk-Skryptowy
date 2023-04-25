#zad2
# def my_func(f, arg):
#     return (f(arg))
#
# print(my_func(lambda x: 2 * x * x, 5))
#
# def func2(x):
#     for i in range(x):
#         print(my_func(lambda x: x ** 2, i + 1))
# func2(4)
#
# #zad3
# tab = [1, 2, 3, 5, 8, 3, 0, 7]
# def func3(x):
#       if x > 4:
#         return False
#       else:
#         return True
#
# result = filter(func3, tab)
#
# for x in result:
#     print(x)

#zad4
# a =['s', 'sp', 'spa', 'spam']
#
#
# def countdown():
#     i = 5
#     while i > 0:
#         yield i
#         i -= 1
# for i in countdown():
#     print(i)
#
#
# def numbers(x):
#     for i in range(x):
#         if i % 2 == 0:
#             yield i
#
# print(list(numbers(11)))
#
# def gen():
#     newList = []
#     it = iter(a)
#     while True:
#         try:
#             x = next(it)
#         except StopIteration:
#             break
#         newList.append(x)
#     print(newList)
# gen()

#zad5
# def func5(x):
#     return 5*(x**2) + 3*x + 8
#
# def decor(func):
#     def wrap():
#         print("Wzór funckji")
#         func()
#         print("==================")
#         print("Wynik")
#     return wrap
#
# def print_function():
#     print("5*(x**2) + 3*x + 8")
#
# decorated = decor(print_function)
# decorated()
# print(func5(4))

#zad6
def Newton(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return n / k * Newton(n - 1, k - 1)

print(Newton(5,3))
