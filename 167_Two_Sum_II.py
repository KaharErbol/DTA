# Two Sum II - Input Array Is Sorted
def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        curr_sum = numbers[l] + numbers[r]
        if curr_sum > target:
            r -= 1
        elif curr_sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []

numbers = [2,7,11,15]
target = 9

print(two_sum(numbers, target))