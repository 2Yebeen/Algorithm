input()
N = set(list(map(int, input().split())))
M = set(list(map(int, input().split())))
print(len(N^M))