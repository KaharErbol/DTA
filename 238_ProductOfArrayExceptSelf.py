def productExceptSelf(nums):
    l = len(nums)
    ans = [1 for _ in range(l)]
    pre = 1
    post = 1

    for i in range(l):
        ans[i] *= pre
        pre *= nums[i]

        ans[l-1-i] *= post
        post *= nums[l-1-i]
    
    return ans

print(productExceptSelf([1,2,3,4]))