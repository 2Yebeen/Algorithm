def solution(sizes):
    w, h = 0, 0
    for i in sizes:
        if w < max(i):
            w = max(i)
        if h < min(i):
            h = min(i)
    answer = w * h
    return answer