from collections import defaultdict
from itertools import product

def solution(clothes):
    answer = 1
    keys = [ k for v, k in clothes]
    counts = [keys.count(key) for key in set(keys)]
    print(keys, counts)
    for c in counts:
        answer *= c + 1
    # 모든 경우에서 의상을 하나도 고르지 않는 경우 제외
    return answer - 1
