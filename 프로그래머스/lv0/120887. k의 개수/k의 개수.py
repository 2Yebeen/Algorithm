def solution(i, j, k):
    answer = 0
    k = str(k)
    for i in range(i, j + 1):
        answer += str(i).count(k)
    return answer