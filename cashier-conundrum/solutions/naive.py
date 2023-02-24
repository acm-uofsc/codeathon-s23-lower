import sys

def minCoins(coins, m, V):
	if (V == 0):
		return 0

	res = sys.maxsize
	
	# Try every coin that has smaller value than V
	for i in range(0, m):
		if (coins[i] <= V):
			sub_res = minCoins(coins, m, V-coins[i])

			if (sub_res != sys.maxsize and sub_res + 1 < res):
				res = sub_res + 1

	return res

x, y = map(int, input().split())
coins = [int(d) for d in input().split()]
m = len(coins)

for _ in range(y):
    value = int(input())
    print(minCoins(coins, m, value))

