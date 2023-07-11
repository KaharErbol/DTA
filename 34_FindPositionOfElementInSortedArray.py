def search_range(nums, target):
    result = [-1, -1]

    result[0] = start_idx(nums, target)
    result[1] = end_idx(nums, target)

    return result

def start_idx(nums, target):
    idx, l, r = -1, 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if target == nums[m]:
            idx = m
            r = m - 1
        elif target < nums[m]:
            r = m - 1
        else:
            l = m + 1
    return idx

def end_idx(nums, target):
    idx, l, r = -1, 0, len(nums) - 1
    while l <= r:
        m = (l+r) // 2
        if target == nums[m]:
            idx = m
            l = m + 1
        elif target > nums[m]:
            l = m + 1
        else:
            r = m - 1
    return idx


nums = [5,7,7,8,8,10] 
target = 8
print(search_range(nums, target))
