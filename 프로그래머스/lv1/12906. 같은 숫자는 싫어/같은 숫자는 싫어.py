def solution(arr):
    ans = [arr[0]]
    for i in range(len(arr)):
        if ans[-1] != arr[i]:
            ans.append(arr[i])
    return ans