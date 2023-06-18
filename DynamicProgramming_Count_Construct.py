"""
Return the number of ways that the target can be
constructed by concatenating the elements of wordBank.
"""
def count_construct(target, wordBank, memo={}):
    if target in memo: return memo[target] 
    if target == "": return 1

    total_count = 0

    for word in wordBank:
        if target.startswith(word):
            count_rest = count_construct(target[len(word):], wordBank, memo)
            total_count += count_rest

    memo[target] = total_count    
    return total_count

print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    "e", 
    "ee",
    "eee",
    "eeee",
    "eeeee",
    "eeeeee",]))