def solution(before, after):
    if sorted(list(before)) == sorted(list(after)):
        return 1
    return 0