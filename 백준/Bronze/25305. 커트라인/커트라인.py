input = __import__('sys').stdin.readline

N, k = list(map(int, input().split()))
lst = sorted(list(map(int, input().split())))
print(lst[-k])