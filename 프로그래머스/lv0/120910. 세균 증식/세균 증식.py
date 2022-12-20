def solution(n, t):
    if t==0:
        return n
    return solution(n+n, t-1)