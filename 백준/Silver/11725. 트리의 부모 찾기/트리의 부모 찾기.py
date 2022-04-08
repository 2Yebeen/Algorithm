import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
n = N + 1
arr = [[] for _ in range(n)]
visited = [0] * n
que = deque()
que.append(1)

for _ in range(1, N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

while que:
    node = que.popleft()
    for x in arr[node]:
        if not visited[x]:
            visited[x] = node
            que.append(x)


print("\n".join(map(str, visited[2:])))