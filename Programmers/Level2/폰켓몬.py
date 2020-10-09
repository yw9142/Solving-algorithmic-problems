def solution(nums):
    max_value = len(nums) // 2
    set_nums = list(set(nums))

    if max_value >= len(set_nums):
        return len(set_nums)
    else:
        return max_value
