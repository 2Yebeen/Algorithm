N = int(input())
grade = list(map(int, input().strip().split(" ")))
M = max(grade)
print((sum(grade)/M*100)/N)