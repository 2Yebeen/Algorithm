total = int(input())
N = int(input())

for _ in range(N):
    cash, cnt = list(map(int, input().split()))
    total -= (cash * cnt)
print("Yes") if total == 0 else print("No")