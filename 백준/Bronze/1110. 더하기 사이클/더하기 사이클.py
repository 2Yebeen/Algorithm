new = int(input())
oldNew = new
x = 0
y = 0
cnt = 0
while 1:
    x = new//10 + new%10 # 1의 자리 10의 자리 더하기
    y = (new%10)*10 + x%10 # 새로운 숫자
    cnt += 1
    new = y
    if new == oldNew:
        break
print(cnt)