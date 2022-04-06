def solution(s):
	s = s.replace("{", '').replace("}",' ').split(" ")
	for i in range(len(s)):
		s[i] = s[i].replace(',',' ').strip().split()
		s[i] = set(map(int, s[i]))
	cnt = len(s)
	ans = []
	while cnt > 0:
		for i in min(s):
			if i not in ans:
				ans.append(i)
		s.remove(min(s))
		cnt-=1
	return ans

s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
s4 = "{{123}}"
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s5))



