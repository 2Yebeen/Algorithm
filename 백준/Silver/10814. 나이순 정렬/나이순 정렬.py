input = __import__('sys').stdin.readline
lst = [input().split() for _ in range(int(input()))]
lst.sort(key=lambda x:int(x[0]))
for x, y in lst:
	print(x, y)