#!/usr/local/bin/python3
from random import randint
case_num = int(input())
# 0 and 1 are the sample cases
if case_num == 0:
    print(1)
    print("encryptpassword")
elif case_num == 1:
    print(2)
    print("Str0ngPassw.?!")
else:
    # output what should be read in as input by
    # contestant code
    word = ""
    n = randint(8, 16)
    j = randint(1, 6)
    i = 0
    while i < n:
        c = randint(33, 116)
        word += chr(c)
        i += 1
    print(j)
    print(word)
