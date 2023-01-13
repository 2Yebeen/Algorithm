from collections import deque

def solution(k, score):
    answer = []
    k_score = []
    for i, s in enumerate(score):
        if len(k_score) == k:
            _score = k_score.pop()
            if s > _score:
                k_score.append(s)
            else:
                k_score.append(_score)
        else:
            k_score.append(s)
        k_score.sort(key=lambda x:-x)        
        answer.append(k_score[-1])
    return answer