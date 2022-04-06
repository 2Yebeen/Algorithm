"""
[계단 오르기]
https://www.acmicpc.net/problem/2579
https://bini-079.tistory.com/106

    input
6
10
20
15
25
10
20
    output
75
"""

import sys
input = sys.stdin.readline

N = int(input())
n = N + 1
dp = [0] * 301
stair = [0] * 301
for x in range(1, n):
    stair[x] = int(input())
dp[1] = stair[1]
dp[2] = stair[1] + stair[2]
for i in range(3, n):
    dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])
print(dp[N])