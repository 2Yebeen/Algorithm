from collections import deque

def solution(progresses, speeds):
    answer = []
    distribute = deque()
    
    for progress, speed in zip(progresses, speeds):
        day = 0
        while progress < 100:
            progress += speed
            day += 1
        distribute.append(day)
    
    start = distribute.popleft()
    cnt = 1
    while distribute:
        next = distribute.popleft()
        if start < next:
            start = next
            answer.append(cnt)
            cnt = 0
        cnt += 1
    answer.append(cnt)
    return answer