import sys
input = sys.stdin.readline
hour = lambda x: x - 24 if x >= 24 else x

A, B = map(int, input().split())
C = int(input())
minute = B + C
A += minute // 60
B = minute % 60
print(hour(A), B)