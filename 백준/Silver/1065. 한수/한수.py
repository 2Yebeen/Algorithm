input = __import__('sys').stdin.readline

def Hansoo(x):
    if int(x[0]) - int(x[1]) == int(x[1]) - int(x[2]):
        return 1
    elif int(x) == 1000:
        return 0
    else:
        return 0

N = int(input())
if N < 100:
    print(N)
else:
    cnt = 99
    for i in range(100, N+1):
        cnt += Hansoo(str(i))
    print(cnt)