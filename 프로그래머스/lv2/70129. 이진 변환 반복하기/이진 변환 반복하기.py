def binary(num):
    save = []
    while True:
        a = int(num / 2)
        b = int(num % 2)
        save.insert(0, b)
        if a != 0:
            num = a
        else:
            break
    return(''.join(map(str, save)))


def getBinaryNum(cnt, ret):
    ret.append(cnt)
    if cnt[1] == 1:
        return ret
    return getBinaryNum([cnt[0] + cnt[2].count('0'), cnt[2].count('1'), binary(cnt[2].count('1'))], ret)


def solution(s):
    ret = []
    getBinaryNum([s.count('0'), s.count('1'), binary(s.count('1'))], ret)
    return [len(ret), ret[-1][0]]