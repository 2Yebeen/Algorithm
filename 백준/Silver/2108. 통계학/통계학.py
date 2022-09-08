input = __import__('sys').stdin.readline

N=int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

print(round(sum(arr)/N))
arr.sort()
print(arr[N//2])

from collections import Counter
k=Counter(arr).most_common()
if len(arr) > 1:
    if k[0][1] == k[1][1]:
        print(k[1][0]) 
    else:
        print(k[0][0]) 
else:
    print(arr[0]) 
print(arr[-1] -  arr[0])