#!/usr/local/bin/python3
from random import randint, choices
case_num = int(input())
if case_num == 0:
    print(4, 2)
    print(25, 10, 5, 1)
    print(75)
    print(33)
elif case_num == 1:
    print(5, 4)
    print(31, 16, 3, 2, 1)
    print(26)
    print(32)
    print(99)
    print(9)
elif case_num <= 35:
    x = randint(3, 8)
    y = randint(1, 10)
    print(x + 2, y)
    denominations = [1, 2] + choices(list(range(3, 50)), k=x)
    denominations = sorted(denominations, reverse=True)
    print(*denominations)
    for _ in range(y):
        print(randint(1, 99))
else:
    x = randint(3, 10)
    y = randint(1, 1000)
    print(x + 2, y)
    denominations = [1, 2] + choices(list(range(3, 50)), k=x)
    denominations = sorted(denominations, reverse=True)
    print(*denominations)
    for _ in range(y):
        print(randint(1, 10000))
