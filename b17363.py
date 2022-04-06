"""
"""
input = __import__('sys').stdin.readline

rli = {'.': '.', 'O': 'O', '-': '|', '|': '-', '/': '\\', '\\': '/', '^': '<', '<': 'v', 'v': '>', '>': '^'}

n, m = map(int,input().strip().split())
box =[list(map(str, input().strip())) for _ in range(n)]

for i in range(m-1,-1,-1):
    for x in box:
        print(rli[x[i]],end='')
    print()
