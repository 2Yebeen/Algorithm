def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        x = 0 if i % 2 == 0 else 1
        answer[x] = answer[x] + 1
    return answer