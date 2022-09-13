def solution(s):
    isSpace = True
    answer = ''
    for i in s:
        if i == ' ':
            isSpace = True
        if isSpace and i != ' ':
            answer += i.upper()
            isSpace = False
        else:
            answer += i.lower()
    return answer