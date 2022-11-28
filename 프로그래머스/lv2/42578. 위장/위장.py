from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)

    for value, key in clothes:
        clothes_dict[key].append(value)

    for i in clothes_dict.keys():
        answer *= len(clothes_dict[i]) + 1
    return answer - 1