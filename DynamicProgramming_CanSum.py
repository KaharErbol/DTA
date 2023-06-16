"""
The function takes two arguments, target int, and an array of nonnegative 
numbers.m Return True if the combination of numbers can generate the target value.
Elements in the array can be used as many times as needed.
"""

def can_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers): 
            memo[remainder] = True
            return True
    memo[remainder] = False
    return False

numbers = [7, 14]
target = 300
print("Target is 14", can_sum(14, [2,3,4,5]))
print(f"Target is {target}", can_sum(target, numbers))
print("Target is 7", can_sum(7, [2,3,4,5]))