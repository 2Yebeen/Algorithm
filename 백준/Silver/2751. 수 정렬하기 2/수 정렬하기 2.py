input = __import__('sys').stdin.readline

N = int(input())
lst = sorted([int(input()) for _ in range(N)])
print('\n'.join(str(i) for i in lst))