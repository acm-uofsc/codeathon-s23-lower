x = input()
y = input()
z = ""

i = 0
while i < len(y):
    z += chr(ord(y[i]) + int(x))
    i += 1
print(z)