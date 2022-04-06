import itertools
def solution(user_id, banned_id):
	ans = 0
	ban = [[] for _ in range(len(banned_id))]
	for i in range(len(banned_id)):
		for x in range(len(banned_id[i])):
			if banned_id[i][x] == "*":
				ban[i].append(x)
	
	print(ban)
	return ans


user1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user2 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
user3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"]

banned1 = ["fr*d*", "abc1**"]
banned2 = ["*rodo", "*rodo", "******"]
banned3 = ["fr*d*", "*rodo", "******", "******"]

print(solution(user2, banned2))