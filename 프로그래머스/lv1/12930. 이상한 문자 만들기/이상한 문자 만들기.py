def solution(s):
	i = 0
	ret = ''
	str = list(s)
	for w in str:
		if w == ' ':
			ret += ' '
			i = 0
			continue ;
		if i % 2 == 0:
			ret += w.upper()
		elif i % 2 != 0:
			ret += w.lower()
		i += 1
	return ret