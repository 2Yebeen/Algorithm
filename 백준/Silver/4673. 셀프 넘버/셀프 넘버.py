numbers = [i for i in range(1, 10001)]
g_num = []
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g_num.append(i)

for x in numbers:
    if x not in g_num:
        print(x)
