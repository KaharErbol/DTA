def combination_sum(nums, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        
        if i >= len(nums) or total > target:
            return
        
        cur.append(nums[i])
        dfs(i, cur, total + nums[i])
        cur.pop()

        dfs(i + 1, cur, total)

    dfs(0, [], 0)

    return res

nums = [2,3,6,7]
target = 7

print(combination_sum(nums, target))