from itertools import combinations, product
def solution(user_id, banned_id):
	ans = 0
	ban_u = [[] for _ in range(len(banned_id))]
	# ban_i = [[] for _ in range(len(banned_id))]
	# for i in range(len(banned_id)):
	# 	for x in range(len(banned_id[i])):
	# 		if banned_id[i][x] == "*":
	# 			ban_i[i].append(x)
	
	for b in banned_id:
		i = 0
		lb = len(b)
		for u in user_id:
			lu = len(u)
			if lb == lu:
				while lb > 0:
				if b[i] != "*" and b[i] != u[i]:
					break
			i += 1
		ban_u.append(u)
	print(ban_u)
	return ans


user1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned1 = ["fr*d*", "abc1**"]
banned2 = ["*rodo", "*rodo", "******"]
banned3 = ["fr*d*", "*rodo", "******", "******"]

print(solution(user2, banned2))