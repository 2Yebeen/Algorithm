from collections import deque

def solution(s):
    s = deque(s)
    answer = 0
    while s:
        w = s.popleft()
        cnt = 1
        while cnt > 0 and s:
            if w == s.popleft():
                cnt += 1
            else:
                cnt -= 1
        answer += 1
    return answer