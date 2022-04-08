input = __import__('sys').stdin.readline
N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N+1):
        if (i%100//10)*2 == (i//100) + (i%100%10): cnt += 1
    print(cnt)
