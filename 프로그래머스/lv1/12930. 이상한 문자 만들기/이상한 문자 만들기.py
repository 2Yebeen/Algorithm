def solution(s):
	i = 0
	ret = ''
	for w in s:
		if w == ' ':
			ret += ' '
			i = 0
			continue ;
		ret += w.upper() if i % 2 == 0 else w.lower()
		i += 1
	return ret
