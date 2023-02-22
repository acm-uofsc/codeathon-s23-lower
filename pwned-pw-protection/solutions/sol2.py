n, m = [int(x) for x in input().split()]
words = [sorted(x) for x in input().split()]
for _ in range(m):
    password = sorted(input())
    for word in words:
        if word == password:
            print('True')
            break
    else:
        print('False')


