#!/usr/local/bin/python3
from random import randint
import random
import string

base = string.ascii_letters + string.digits + string.punctuation

case_num = int(input())
if case_num == 0:
    print(1, 1)
    print('listen')
    print('silent')
elif case_num == 1:
    print(5, 3)
    print('Alphabet', 'Toll', 'Password123!', '120j3ufdsaofsd', 'PotatoPie451')
    print('alphabet')
    print('Lot')
    print('123Password!')
elif case_num <= 35:
    n = randint(100, 1000)
    m = randint(100, 1000)
    word_len = randint(100, 1000)
    print(n, m)
    words = []
    for _ in range(n):
        words.append(''.join(random.choices(base, k=word_len)))
    print(*words)
    for _ in range(m):
       print(''.join(random.choices(base, k=word_len))) 
else:
    n = randint(100, 1000)
    m = randint(10, 100)
    word_len = randint(10, 10000)
    print(n, m)
    words = []
    for _ in range(n):
        words.append(''.join(random.choices(base, k=word_len)))
    print(*words)
    for _ in range(m):
       print(''.join(random.choices(base, k=word_len))) 
