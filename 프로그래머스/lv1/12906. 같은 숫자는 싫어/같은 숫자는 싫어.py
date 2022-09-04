def solution(arr):
    ans = [arr[0]]
    a = 0
    for i in range(len(arr)):
        if ans[a] != arr[i]:
            ans.append(arr[i])
            a += 1
    return ans