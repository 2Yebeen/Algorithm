def solution(k, m, score):
    ans = 0
    score.sort(reverse=True)
    for i in range(m-1, len(score), m):
        ans += (score[i] * m) 
    return ans