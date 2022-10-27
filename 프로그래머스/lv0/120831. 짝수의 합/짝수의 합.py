def solution(n):
    ans = 0
    for i in range(2, n+1, 2):
        ans += i
    return ans