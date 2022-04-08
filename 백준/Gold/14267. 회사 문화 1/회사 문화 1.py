import sys
input = sys.stdin.readline

n, m = map(int, input().split())
superior = list(map(int, input().split()))
compliment = [0] * n

for _ in range(m):
    i, w = map(int, input().split())
    compliment[i - 1] += w

for i in range(1, n):
    compliment[i] += compliment[superior[i] - 1]

print(*compliment)