#задание 1
from modul_new import salary
salary_per_hour = int(input ("Введите ставку в час, руб: "))
hours_total = int(input("Введите выработку в часах: "))
prize = int(input("Введите сумму премии, руб: "))
salary(salary_per_hour, hours_total, prize)
#задание 2
random_list = [65, 79, 12, 4, 88, 64, 99, 44, 76, 96]
total_list = [el for i, el in enumerate(random_list) if i > 0 and random_list[i] > random_list[i- 1]]
print(total_list)
#задание 3
total_range = print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])
#задание 4 вариант1
numbers_list = [3, 4, 5, 3, 4 , 5, 33, 34, 87, 33, 49, 88, 74]
numbers_list_new = [el for el in numbers_list if numbers_list.count(el) <= 1]
print(numbers_list_new)
import math
list_form = print(math.prod([el for el in range(100, 1001) if el % 2 == 0]))
#задание 4 вариант2
from functools import reduce
def list_new(prev_el, el):
    return prev_el*el
print(reduce(list_new, [el for el in range(100, 1001) if el % 2 == 0]))
#задание 6
from itertools import count
for a in count(5):
     if a > 10:
        break
     else:
         print(a)
from itertools import cycle
g = ["Hello, world", "Hello, space"]
e = 0
for el in cycle(g):
     if e > 10:
         break
     print(el)
     e += 1
#задание 7
n = int(input("Введите n: "))
u = [i for i in range(1,n+1)]
def factorial(u):
    list_4 = [el*(el+2) for el in u]
    yield list_4
print(list(factorial(u)))
