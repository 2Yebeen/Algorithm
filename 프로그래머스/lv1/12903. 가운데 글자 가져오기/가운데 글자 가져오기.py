def solution(s):
    answer = ''
    print(len(s)//2)
    if len(s) % 2 == 0:
        return s[len(s)//2-1]+s[len(s)//2]
    return s[len(s)//2]