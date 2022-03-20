"""
https://www.acmicpc.net/problem/1916
problem
N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 
우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 
A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.
input
첫째 줄에 도시의 개수 N(1 ≤ N ≤ 1,000)이 주어지고 둘째 줄에는 버스의 개수 M(1 ≤ M ≤ 100,000)이 주어진다. 
그리고 셋째 줄부터 M+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
그리고 M+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다. 
출발점에서 도착점을 갈 수 있는 경우만 입력으로 주어진다.
output
첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
    input
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
    output
4
"""
import sys
from heapq import heappush, heappop
input = sys.stdin.readline # 빠른 입력
INF = int(1e9)              # 무한을 의미하는 값으로 10억 설정

N = int(input())            # 노드의 개수
M = int(input())            # 간선의 개수를 입력받기
distance = [INF]*(N+1)      # 최단거리 테이블(각 정점사이의 거리 무한대로 초기화)

# 노드 연결정보
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # a번노드에서 b번 노드로 가는 비용c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# 출발 노드와 도착 노드 번호를 입력받기
start, end = map(int, input().split())

# 다익스트라 알고리즘(최소힙 이용))
def dijkstra(start):
    heap = []
    # 시작 노드
    heappush(heap, (0, start))
    distance[start] = 0 # 시작 지점 0으로 초기화
    
    while heap:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(heap)
        # 이미 처리된 노드였다면 무시
        # 별도의 visited 테이블이 필요없이, 최단거리테이블을 이용해 방문여부 확인
        if distance[now] < dist:
            continue
        # 선택된 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


# 다익스트라 알고리즘수행
dijkstra(start)

# 도착 노드로 가기 위한 최단 거리를 출력
print(distance[end])
