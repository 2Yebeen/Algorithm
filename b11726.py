"""
[2×n 타일링] - 다이나믹 프로그래밍
https://www.acmicpc.net/problem/11726

    input
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
    output
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

    input 1
2
    output 1
2
    input 2
9
    output 2
55
"""

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (n+1)
if n < 3:
    print(n % 10007)
else:
    dp[1], dp[2] = 1, 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n] % 10007)