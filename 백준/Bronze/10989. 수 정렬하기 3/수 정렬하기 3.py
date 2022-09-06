input = __import__('sys').stdin.readline

n = int(input())
lst = [0] * 10001
for _ in range(n):
	i = int(input())
	lst[i] += 1

for i in range(1, 10001):
	while lst[i] != 0:
		print(i)
		lst[i] -= 1
