def majorityElement(nums):

    res = None
    cnt = 0

    for num in nums:
        if cnt == 0:
            res = num
        
        if num == res:
            cnt += 1
        else:
            cnt -= 1
    return res

def majorityElement2(nums):
    uni_elements = set(nums)
    length = len(nums) / 2
    for each in uni_elements:
        count = nums.count(each)
        if count >= length:
            return each
    return -1

nums = [2,2,1,1,1,2,2]

print("1st method: ", majorityElement(nums))
print("2nd method: ", majorityElement2(nums))