def make_change(target, coins, coins_so_far):
	if sum(coins_so_far) == target:
		yield coins_so_far
	elif sum(coins_so_far) > target:
		pass
	elif coins == []:
		pass
	else:
		for c in change(target, coins[:], coins_so_far+[coins[0]]):
			yield c
		for c in change(target, coins[1:], coins_so_far):
			yield c

if __name__ == '__main__':
	n = 19
	coins = [10, 7, 5, 3, 1]
	solutions = [s for s in change(n, coins, [])]
	print('optimal solution:', min(solutions, key=len))
