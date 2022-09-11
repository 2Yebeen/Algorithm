def solution(a, b):
    if a > b:
        a, b = b, a
    answer = b
    for i in range(a, b):
        answer += i
    return answer