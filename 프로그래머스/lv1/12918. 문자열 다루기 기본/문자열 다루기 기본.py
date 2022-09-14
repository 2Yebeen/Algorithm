def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for i in s.lower():
        print(i)
        if i in "abcdefghijklmnopqrstuvwxyz":
            return False
    return True