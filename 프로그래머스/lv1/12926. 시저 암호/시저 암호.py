def solution(s, n):
    answer = ''
    for i in s:
        if (97 <= ord(i) and ord(i) <= 122) or (65 <= ord(i) and ord(i) <= 90):
            if (97 <= ord(i) and ord(i) <= 122) and ord(i) + n > 122:
                answer += chr(ord(i) + n - 122 + 96)
            elif (65 <= ord(i) and ord(i) <= 90) and ord(i) + n > 90:
                answer += chr(ord(i) + n - 90 + 64)
            else:
                answer += chr(ord(i) + n)
        else:
            answer += i
    return answer