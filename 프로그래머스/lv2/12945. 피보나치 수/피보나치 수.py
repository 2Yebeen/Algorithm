def solution(n):
    ret = 0
    fibo = [0, 1]
    for i in range(n-1):
        fibo.append(fibo[i] + fibo[i+1])
    return fibo[n] % 1234567
