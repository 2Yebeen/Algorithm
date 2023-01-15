import math

def primenumber(x):
    for i in range (2, int(math.sqrt(x) + 1)):
    	if x % i == 0:
        	return 0
    return 1

                    
def solution(n):
    ans = 0
    for i in range(2, n + 1):
        ans += primenumber(i)
    return ans