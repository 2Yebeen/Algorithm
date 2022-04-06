import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
delete = int(input())
leaf = 0


def dfs(x):
    arr[x] = -10
    for i in range(N):
        if arr[i] == x:
            dfs(i)
            
            
dfs(delete)
for i in range(N):
    if arr[i] != -10 and i not in arr:
        leaf += 1
print(leaf)