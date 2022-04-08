import sys
import copy
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
count = 0
virus = deque()


def spread():
    global count
    cnt = 0
    tmp = copy.deepcopy(lab)
    for r in range(N):
        for c in range(M):
            if tmp[r][c] == 2:
                virus.append((r, c))

    while virus:
        x, y = virus.popleft()
        for i in range(4):
            row, col = x + dr[i], y + dc[i]
            if 0 <= row < N and 0 <= col < M and not tmp[row][col]:
                tmp[row][col] = 2
                virus.append((row, col))
    for i in tmp:
        for j in i:
            if not j:
                cnt += 1
    count = max(count, cnt)


def wall(start, cnt):
    if cnt == 0:
        spread()
        return
    for i in range(start, N*M):
        x = i // M
        y = i % M
        if not lab[x][y]:
            lab[x][y] = 1
            wall(i+1, cnt-1)
            lab[x][y] = 0


wall(0, 3)
print(count)