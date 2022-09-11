input = __import__('sys').stdin.readline
pos = sorted([list(map(int, input().strip().split())) for _ in range(int(input().strip()))])
for x, y in pos:
    print(x, y)
