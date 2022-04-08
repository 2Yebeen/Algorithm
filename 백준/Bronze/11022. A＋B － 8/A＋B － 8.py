import sys
n = int(input())
for x in range(1,n+1):
    a,b = map(int,sys.stdin.readline().split(" "))
    print("Case #%d: %d + %d = %d"%(x,a,b,a+b))