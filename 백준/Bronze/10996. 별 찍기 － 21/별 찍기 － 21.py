n = int(input())
star = ["*"]
if n%2 == 0:
    for i in range(n):
        print(*star*(n//2))
        print("",*star*(n//2))
elif n == 1:
    print("*")
else:
    for i in range(n):
        print("*", *star * ((n - 1) // 2))
        print("", *star * ((n - 1) // 2))