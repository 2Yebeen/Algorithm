num1, num2 = map(str, input().split())
num1 = int(num1[::-1])
num2 = int(num2[::-1])
print(num1) if num1 > num2 else print(num2)