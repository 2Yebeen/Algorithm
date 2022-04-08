import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
data = map(str, range(1, N+1))
print('\n'.join(list(map(' '.join, permutations(data, M)))))