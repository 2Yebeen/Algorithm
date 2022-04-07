R, B = map(int,input().strip().split(" "))
v = (R + B)**0.5 # 제곱근
for L in range(1, int(v+1)) :
    W = (R+B) // L
    if L * W == R + B and R == (L+W) * 2 - 4 :#L * 2 + W * 2 - 4 :
        print(W, L)
        break