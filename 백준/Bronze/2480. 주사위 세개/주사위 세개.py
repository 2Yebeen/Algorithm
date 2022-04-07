import sys
input = sys.stdin.readline

diceArr = sorted(map(int, input().split()))
dice_len = len(set(diceArr))
print(diceArr[dice_len - 1]*[100, 1000][dice_len == 1] + [10000, 1000, 0][dice_len - 1])
