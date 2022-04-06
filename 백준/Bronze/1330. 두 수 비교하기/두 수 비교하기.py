s = input() # 1 2
li = s.split(" ") # li = ['1', '2']
a = int(li[0])
b = int(li[1])
if a > b :
    print(">")
elif a < b :
    print("<")
else:
    print("==")