def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    sorted_nums = sorted(nums)
    table = {}

    for i in range(len(nums)):
        num = sorted_nums[i]
        if num not in table:
            table[num] = i
    
    return [table[num] for num in nums]


