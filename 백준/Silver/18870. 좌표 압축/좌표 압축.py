input = __import__('sys').stdin.readline
N = int(input())
lst = list(map(int, input().split()))
slst = sorted(list(set(lst)))
dic = { slst[i] : i for i in range(len(slst)) }
print(' '.join(str(dic[i]) for i in lst))