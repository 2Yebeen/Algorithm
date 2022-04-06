def solution(board, moves):
	ans = 0
	n = []
	for i in moves:
		for j in range(len(board)):
			if board[j][i-1]:
				# if len(n) > 1 and n[len(n)-1] == board[j][i-1] :
				# 	n.pop()
				# 	ans += 2
				# 	break
				n.append(board[j][i-1])
				break
		board[j][i-1] = 0
		if len(n) > 1 and n[-1] == n[-2]:
			ans += 2
			n.pop()
			n.pop()
	return ans


board1 = [
	[0,0,0,0,0],
	[0,0,1,0,3],
	[0,2,5,0,1],
	[4,2,4,4,2],
	[3,5,1,3,1]
]
moves1 = [1,5,3,5,1,2,1,4]
print(solution(board1, moves1))

