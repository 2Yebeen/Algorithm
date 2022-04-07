bugger = []
soda = []
for i in range(3):
    bugger.append(int(input()))
for x in range(2):
    soda.append(int(input()))
print(int(min(bugger))+int(min(soda))-50)