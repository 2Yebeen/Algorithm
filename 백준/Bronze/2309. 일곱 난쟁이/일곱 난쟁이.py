li = [0]*9
for x in range(9):
    li[x] = int(input())
li.sort() # 원본 정렬
total = sum(li)
for a in range(9) : # 제거할 원소 1
    for b in range(9) : # 제거할 원소 2
        if a == b : continue
        if total - li[a] - li[b] == 100 :
            for x in range(9) :
                if x == a or x == b : continue
                print(li[x])
            exit(0)