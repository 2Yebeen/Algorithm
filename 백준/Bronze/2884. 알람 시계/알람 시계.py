alarm = input()
li = alarm.split(" ")
h = int(li[0])
m = int(li[1])
if (m - 45) < 0 :
    h = h - 1
    m = m + 60 - 45
elif m == 60:
    m = m - 45
elif (m - 45) > 0:
    m = m - 45
else:
    m = 0
if h < 0:
    h = h+24
print(h,m)