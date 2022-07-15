input = __import__('sys').stdin.readline

N = int(input())
for _ in range(N):
    cnt, lst = map(str, input().split())
    for i in range(len(lst)):
        print(lst[i] * int(cnt), end = "")
    print()