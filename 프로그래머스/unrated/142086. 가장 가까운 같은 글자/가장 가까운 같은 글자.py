def solution(s):
    answer = []
    for i in range(len(s)):
        new_s = s[:i]
        if s[i] not in new_s:
            answer.append(-1)
        else:
            rev_s = new_s[::-1]
            answer.append(rev_s.index(s[i])+1)
    return answer