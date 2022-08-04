dial = ['', '', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
number = input()
time = 0
for i in range(len(number)):
    for j in range(3, 11):
        if number[i] in dial[j]:
            time += j
print(time)