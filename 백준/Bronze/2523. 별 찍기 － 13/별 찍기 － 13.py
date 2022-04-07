n = int(input())
for i in range(1,n+1):
    print("*"*i)
    if i == n:
        for x in range(1,n):
            n -= 1
            print("*"*n)