N = int(input()) # N(1<=N<=1,000,000)
li = [0] * 1000001
for i in range(N//10, N) : 
    num = i
    분해합 = num # 자기 자신 숫자도 더하기
    while num > 0 : # 각자리수 짤라내기
        분해합 += num % 10 # 일의 자리 추출
        num //= 10
    if 분해합 < 1000001 and li[분해합] == 0:
        li[분해합] = i
print(li[N])