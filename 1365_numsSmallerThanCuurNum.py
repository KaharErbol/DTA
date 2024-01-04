def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    nums_sorted = sorted(nums)
    table = {}
    
    for i in range(len(nums_sorted)):
        if nums_sorted[i] not in table:
            table[nums_sorted[i]] = i
            
    res = [table[num] for num in nums]

    return res

nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))