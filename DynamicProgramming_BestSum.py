"""
FInd the shortest combination of numbers to generate the target value
"""

def best_sum(target, numbers, memo={}):
    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0 : return None
    shortest_combo = None
    for num in numbers:
        remainder = target - num
        remainder_combo = best_sum(remainder, numbers, memo)
        if remainder_combo is not None:
            new_combo = remainder_combo + [num]
            if shortest_combo is None or len(new_combo) < len(shortest_combo):
                shortest_combo = new_combo

    memo[target] = shortest_combo
    return shortest_combo


print(best_sum(11, [1,2,5]))