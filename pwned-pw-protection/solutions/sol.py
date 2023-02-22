from collections import Counter

n, m = [int(x) for x in input().split()]
database = [Counter(x) for x in input().split()]
for _ in range(m):
    password = Counter(input())
    for entry in database:
        if entry == password:
            print('True')
            break
    else:
        print('False')
