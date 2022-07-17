input = __import__('sys').stdin.readline

n, M = map(int, input().split())
N = n + 1
numbers = map(int, input().split())
sum = [0] * N

for i, num in enumerate(numbers):
    sum[i + 1] = sum[i] + num
for _ in range(M):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])