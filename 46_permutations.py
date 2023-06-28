def permute_1(nums):
    res = []
    if len(nums) == 1:
        return [nums[:]]
    
    for i in range(len(nums)):
        cur = nums.pop(0)
        permutes = permute_1(nums)
        for p in permutes:
            p.append(cur)
        res.extend(permutes)
        nums.append(cur)
    
    return res

def permute_2(nums):
    res = []

    def backtrack(nums, path):
        if len(nums) == 0:
            res.append(nums)

        for i in range(len(nums)):
            remains = nums[:i]+nums[i+1:]
            backtrack(remains, path + [nums[i]])

    backtrack(nums, [])
    
    return res