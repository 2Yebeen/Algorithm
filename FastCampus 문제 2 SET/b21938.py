"""
[백준/21938] - 영상처리
https://www.acmicpc.net/problem/21938

화면에 있는 물체의 개수를 출력하라. 만약 물체가 없으면 0을 출력하면 된다.
--------------------
	input 1
3 3
255 255 255 100 100 100 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255
101
	output 1
5
	input 2
2 2
124 150 123 100 100 100
103 103 103 183 5 3
255
	output 2
0
"""
"""
#상, 하, 좌, 우 체크
dr, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
while
=> 처음 255발견하면 cnt + 1 and 발견한 255와 인접해있는 255를 -1으로 변경,
monitor = [[R, G, B],...]
255 255 255 100 100 100 255 255 255
100 100 100 255 255 255 100 100 100
255 255 255 100 100 100 255 255 255

255 100 255
100 255 100
255 100 255

101

255 0 255
0  255  0
255 0 255

124 150 123 100 100 100
103 103 103 183 5 3

135 100
103 65

255

0 0
0 0
"""
from collections import deque
input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

# 입력
N, M = MIIS()
pixels = []
screen = [[] for _ in range(M)]
visited = [[True] * M for _ in range(N)]
for _ in range(N):
	pixels.append(list(MIIS()))
T = int(input())

# 화면 값 계산
for i in range(N):
	for j in range(0,M*3,3):
		tmp = sum(pixels[i][j:j+3])/3
		if tmp > T :
			screen[i].append(255)
		else:
			screen[i].append(0)
# 물체 계산
que = deque()
visited[0][0] = False
que.append((0, 0))
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
while que:
	r, c = que.popleft()
	if screen[r][c] == 255:
		cnt += 1
	for x in range(4):
		r += dr[x]
		c += dc[x]
		while 0 <= row < N and 0 <= col < M and lab[row][col] == 255 :
			visited[row][col] = False
			if wind_rotate[lab[row][col]][i] != 9:
				i = wind_rotate[lab[row][col]][i]
			else : break
			row += dr[i]
			col += dc[i]

print(cnt)