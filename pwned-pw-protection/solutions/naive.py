n, m = map(int, input().split())
passwords = input().split()
# passwords = {tuple(sorted(word)) for word in passwords}
assert len(passwords) == n
def check(user):
    for password in passwords:
        if len(user) != len(password):
            continue
        password_used = []
        for j in range(len(user)):
            found = False
            for i in range(len(password)):
                if user[j] == password[i] and i not in password_used:
                    password_used.append(i)
                    found = True
                    break
            if not found:
                break
        if len(password_used) == len(password):
            return True
    return False
for i in range(m):
    user = input()
    print(check(user))