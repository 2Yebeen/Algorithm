def solution(s):
    slist = list(map(int, s.split()))
    return ('{} {}'.format(min(slist), max(slist)))