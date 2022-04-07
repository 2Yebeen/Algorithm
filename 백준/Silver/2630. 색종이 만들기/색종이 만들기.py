n = int(input())
color =  [list(map(int, input().split())) for _ in range(n)]

w = 0; # 흰색
b = 0; # 파랑색

def div(x, y, n):
    global w, b
    ch = color[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if ch != color[i][j]:           # 색이 하나라도 같지 않은 경우
                div(x,y,n//2)               # 1 (0,0)
                div(x,y+n//2,n//2)          # 2 (0,1)
                div(x+n//2,y,n//2)          # 3 (1,0)
                div(x+n//2,y+n//2,n//2)     # 4 (1,1)

                return
    if ch == 0:                             # 흰색일 경우
        w += 1
        return
    elif ch == 1:                           # 파란색일 경우
        b += 1
        return

div(0,0,n)
print(w)
print(b)