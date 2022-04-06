"""
[1, 2, 3 더하기]
https://www.acmicpc.net/problem/9095

    input
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 정수 n이 주어진다. n은 양수이며 11보다 작다.
3
4
7
10
    output
각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력한다.
7
44
274
"""
import sys
input = sys.stdin.readline

TC = int(input())   		  # 테스트 케이스
dp = [0] * 11				  # 정수 n을 저장할 리스트(0 < n < 11)
dp[1], dp[2], dp[3] = 1, 2, 4 # 초깃값 세팅 f(n-3)+f(n-2)+f(n-1)

for _ in range(TC):			  # 테스트 케이스 수 많큼 반복
    n = int(input())
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])