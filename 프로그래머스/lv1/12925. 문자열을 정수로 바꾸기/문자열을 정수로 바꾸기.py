def solution(s):
    answer = 0
    sign = 1
    start = 0
    if s[0] == '-':
        sign = -1
    if s[0] == '-' or s[0] == '+':
        start = 1
    for i in range(start,len(s)):
        answer = answer * 10 + int(s[i])
    return answer * sign