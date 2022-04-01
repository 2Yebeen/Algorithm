"""
[백준/21937] - 작업
https://www.acmicpc.net/problem/21937

민상이가 작업 X를 하기 위해 먼저 해야하는 일의 개수를 출력한다.
--------------------
	input 1
6 4
1 6
2 4
4 6
4 5
5
	output 1
2
	input 2
6 4
1 6
2 4
4 6
4 5
3
	output 2
0
	inbput 3
4 4
1 2
1 3
2 4
3 4
4
	output 3
3
"""

input = __import__('sys').stdin.readline
MIIS = lambda: map(int, input().split())

N,M = MIIS()

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = MIIS()
    graph[y].append(x)


start = int(input())
stack = [start]
cnt = 0
visited = [True for _ in range(N+1)]
visited[start] = False
while stack:
    x = stack.pop()

    for next_node in graph[x]:
        if visited[next_node]:
            visited[next_node] = False
            cnt += 1
            stack.append(next_node)

print(cnt)