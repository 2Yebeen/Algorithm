input = __import__('sys').stdin.readline

N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N+1):
        x = str(i)
        if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]): cnt += 1
    print(cnt)