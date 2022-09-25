def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    B.reverse()
    print(A, B)
    for i in range(len(A)):
        answer += (A[i] * B[i])

    return answer