n=int(input())
for x in range(1,n+1):
    print(" " * (x-1) + '*' * (2*n-1))
    n -= 1
    if n == 0:
        for i in range(1,x):
            print(" " * (x-2) + '*' * (2*i+2-1))
            x -= 1