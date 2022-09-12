def solution(n):
    if n == 1:
        return '수'
    if n % 2 == 0:
        return '수박' * (n//2)
    return ('수박' * (n//2)) + '수'