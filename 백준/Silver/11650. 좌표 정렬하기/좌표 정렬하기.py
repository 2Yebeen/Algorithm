input = __import__('sys').stdin.readline
pos = [list(map(int, input().strip().split())) for _ in range(int(input().strip()))]
pos.sort(key = lambda x :(x[0], x[1]))
for x, y in pos:
    print(x, y)
