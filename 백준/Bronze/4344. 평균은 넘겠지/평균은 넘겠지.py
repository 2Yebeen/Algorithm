import sys
for i in range(int(input())) :
    li = list(map(int,sys.stdin.readline().strip().split(" ")))
    cnt = 0
    avg = sum(li[1:])/li[0]
    for i in range(1,len(li)) :
        if li[i] > avg :
            cnt += 1
    print("%.3f"%round((cnt/li[0]*100),3),end="%\n")