def solution(s):
    answer = True
    cnt = 1
    if s[0] == ')' or s[-1] == '(': return False
    for i in range(1, len(s)):
        if s[i] == '(': cnt += 1
        elif s[i] == ')': cnt -= 1
        if cnt < 0: break ;
    return True if cnt == 0 else False