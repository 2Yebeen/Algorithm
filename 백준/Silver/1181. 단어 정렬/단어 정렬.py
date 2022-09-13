data_list = sorted(list(set([input() for _ in range(int(input()))])))
data_list.sort(key=lambda x : len(x))

print(*data_list, sep='\n')