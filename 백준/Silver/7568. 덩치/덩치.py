# 7568 - 덩치
"""
우리는 사람의 덩치를 키와 몸무게, 이 두 개의 값으로 표현하여 그 등수를 매겨보려고 한다.
1. 첫 줄에는 전체 사람의 수 N이 주어진다. 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
2. 여러분은 입력에 나열된 사람의 덩치 등수를 구해서 그 순서대로 첫 줄에 출력해야 한다. 단, 각 덩치 등수는 공백문자로 분리되어야 한다.
"""

N = int(input())
rank = [1] * N
bulk = []
for i in range(N):
    bulk.append(list(map(int, input().split())))

# rank = sorted(bulk, key=lambda x:[-x[0],-x[1]])
for i in range(N-1):
    for j in range(i, N):
        if bulk[i][0] < bulk[j][0] and bulk[i][1] < bulk[j][1]:
            rank[i] = rank[i] + 1
        elif bulk[i][0] > bulk[j][0] and bulk[i][1] > bulk[j][1]:
            rank[j] = rank[j] + 1
print(*rank)