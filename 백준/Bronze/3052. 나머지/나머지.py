li = [int(input()) for x in range(10)]
li = [i % 42 for i in li]
s = set(li)
print(len(s))