import sys
from collections import deque

input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    N, K = map(int, input().split())
    n = N + 1
    time = [0] + list(map(int, input().split()))
    rule = [[] for i in range(n)]
    visited = [0] * n
    ans = [0] * n
    que = deque()

    for _ in range(K):
        x, y = map(int, input().split())
        rule[x].append(y)
        visited[y] += 1

    for i in range(1, n):
        if not visited[i]:
            que.append(i)
            ans[i] = time[i]

    while que:
        now = que.popleft()
        for next in rule[now]:
            visited[next] -= 1
            ans[next] = max(ans[now] + time[next], ans[next])
            if not visited[next]:
                que.append(next)

    print(ans[int(input())])