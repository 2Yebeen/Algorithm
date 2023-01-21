def solution(dartResult):
    ans = []
    n, num = 0, 0
    for i in range(len(dartResult)):
        if dartResult[i] in ['S', 'D', 'T']:
            num = int(dartResult[n:i])
            n = i + 1
            if dartResult[i] == 'D':
                num = num ** 2
            if dartResult[i] == 'T':
                num = num ** 3
            ans.append(num)
        if dartResult[i] in ['*', '#']:
            n += 1
            if dartResult[i] == '*':
                tmp = []
                tmp.append(ans.pop() * 2)
                if ans:
                    tmp.insert(0, ans.pop() * 2)
                ans = ans + tmp
            if dartResult[i] == '#':
                num = ans.pop() * -1
                ans.append(num)
    return sum(ans)