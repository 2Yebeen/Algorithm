li = [0]*9
li = [int(input()) for x in range(9)]
M = max(li)
print(M, li.index(M)+1, sep="\n")