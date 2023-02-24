x, y = map(int, input().split())
denominations = [int(d) for d in input().split()]
assert len(denominations) == x

for _ in range(y):
    coins = 0
    change = int(input())
    output = []
    for value in denominations:
        num_coin = change // value
        coins += num_coin
        change = change % value
        output.append(num_coin)
    print(*output)
