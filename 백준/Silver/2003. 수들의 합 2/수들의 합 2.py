import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0
num_sum = 0
end = 0

for start in range(N):
    while num_sum < M and end < N:
        num_sum += numbers[end]
        end += 1
    if num_sum == M:
        cnt += 1
    num_sum -= numbers[start]

print(cnt)