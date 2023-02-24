offset = int(input())
pw = input()
print(*[chr(ord(c) + offset) for c in pw], sep='')