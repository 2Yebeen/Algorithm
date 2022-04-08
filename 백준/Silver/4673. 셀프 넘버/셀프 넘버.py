numbers = set(range(1, 10001))
g_num = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    g_num.add(i)

self_num = sorted(numbers - g_num)
print('\n'.join(list(map(str, self_num))))