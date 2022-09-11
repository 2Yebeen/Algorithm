def find(str, w):
    cnt = 0
    for i in str:
        if i == w:
            cnt += 1
    return cnt


def solution(s):
    p_cnt = find(s.lower(), 'p')
    y_cnt = find(s.lower(), 'y')
    if (p_cnt == y_cnt) or (p_cnt == 0 and y_cnt == 0):
        return True
    return False