def solution(nums):
    n = len(nums) / 2
    new_nums = list(set(nums))
    if n >= len(new_nums): 
        return len(new_nums)
    else:
        return n
