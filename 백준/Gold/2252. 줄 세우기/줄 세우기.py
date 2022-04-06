import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def line_up(i):
    # 방문 확인
    if visited[i]:
        return
    # 앞에 있어야 할 리스트가 있을 경우 처리
    for next in height[i]:
        line_up(next)
    # 방문 처리, 줄 세우기
    visited[i] = True
    line.append(i)


# N 학생 번호, M 키 비교 횟수
N, M = map(int, input().split())
n = N + 1
# 키 입력 저장
height = [[] for i in range(n)]
# 방문
visited = [False] * n
# 정답 저장
line = []

for _ in range(M):
    a, b = map(int, input().split())
    # b번 인덱스 앞에 와야할 a저장
    height[b].append(a)

# 학생 번호로 줄 세우기
for i in range(1, n):
    line_up(i)

print(' '.join(list(map(str, line))))