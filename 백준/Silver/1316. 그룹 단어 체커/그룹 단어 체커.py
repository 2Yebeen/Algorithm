imput = __import__('sys').stdin.readline

def groupChecker(word):
    prev = ""
    visited = []
    for w in word:
        if prev == w:
            continue
        if w in visited:
            return 0
        else:
            visited.append(w)
        prev = w
    return 1

N = int(input())
cnt = 0
for _ in range(N):
    cnt += groupChecker(input())

print(cnt)