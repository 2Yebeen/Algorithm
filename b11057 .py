"""
[백준/11057] 오르막 수
https://www.acmicpc.net/problem/11057
https://bini-079.tistory.com/107

input / output
1) 1 / 10
2) 2 / 55
3) 3 / 220
"""
import sys
input = sys.stdin.readline

n = int(input())
dp = [1] * 10 # 0 ~ 9 자릿수
# 1의 자리가 0인 경우를 제외하고 2의 자리부터 계산하게 된다.
for _ in range(1, n) :
    for i in range(1, 10) :
        dp[i] += dp[i-1]
# n = 2, dp[2] = dp[2] + dp[1]이 된다 => dp[2] : 1(2의 1의 자릿값) + dp[1] : 2(1의 2의 자릿값)
print(sum(dp)%10007)