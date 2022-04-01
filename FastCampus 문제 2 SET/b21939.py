"""
recommend  1 : 문제 리스트에서 가장 어려운 문제의 번호를 출력(만약 가장 어려운 문제가 여러 개라면 문제 번호가 큰 것을 출력)
recommend -1 : 문제 리스트에서 가장 쉬운 문제의 번호를 출력(가장 쉬운 문제가 여러개라면 문제 번호가 작은 것을 출력)

add P(문제번호) L(난이도) : 추천 문제 리스트에 난이도가 L 인 문제 번호 P를 추가

solved P(문제번호) : 문제번호 P를 제거
"""

input = __import__('sys').stdin.readline

def recommend(x):
	if x == 1:
		pass
	elif x == -1:
		pass

def add(p, l):
	pass

def solved(p):
	pass

# 추천 문제 리스트에 있는 문제의 개수
N = int(input())
lst = [0] * 101
for i in range(N):
	# 문제번호와 난이도가 주어진다.
	P, L = map(int, input().split())
	if lst[L] == 0:
		lst[L] = P
	else:
		lst.insert(L, P)

M = int(input())
for j in range(M):
	tmp = list(map(str, input().split()))
	if tmp[0] == 'recommend':
		recommend(int(tmp[1]))
	if tmp[0] == 'add':
		add(int(tmp[1]), int(tmp[2]))
	if tmp[0] == 'solved':
		solved(int(tmp[1]))