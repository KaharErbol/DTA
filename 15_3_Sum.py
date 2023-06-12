def three_sum(nums):
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            curr_sum = nums[i] + nums[l] + nums[r]
            if curr_sum < 0:
                l += 1
            elif curr_sum > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))