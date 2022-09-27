def solution(n):
    cnt = 0
    for i in range(1, n+1):
        sum = 0
        j = i
        while (j <= n and sum <= n):
            sum += j
            j+= 1
            if sum == n:
                cnt += 1
    return cnt