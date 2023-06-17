"""
How many ways the elements in the arr can generate the target value?
"""

def how_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0 : return None

    for num in  numbers:
        remainder = target - num
        remainder_res = how_sum(remainder, numbers)
        if remainder_res is not None:
            res = remainder_res + [num]
            memo[target] = res
            return res
    memo[target] = None
    return None

print(how_sum(7, [2,3,4,5,7]))
print(how_sum(300, [7, 14]))