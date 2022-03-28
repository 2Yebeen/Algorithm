"""
[백준/21920] - 서로소 평균

첫째 줄에 수열 A에서 X와 서로소인 수들의 평균을 출력한다.
절대/상대 오차는 10-6까지 허용한다.

    input
5
4 2 8 5 7
4
    output
6
----------
"""
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        r = max(a, b) % min(a, b)
        a = min(a, b)
        b = r
    return a


N = int(input())
A = list(set(map(int, input().split())))
X = int(input())
numbers = []
for num in A:
    if gcd(num, X) == 1:
        numbers.append(num)
print(int(sum(numbers)/len(numbers)))
