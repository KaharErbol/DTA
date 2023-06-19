"""
Return a 2D array containing all of the ways
that the target can be constructed by concatenating
elements of wordBank.
"""

def all_construct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == "": return [[]]

    result = []
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordBank)
            target_ways = [[word] + way for way in suffix_ways]
            result += target_ways
    
    memo[target] = result
    return result

print(all_construct("purple", ["purp", "p", "ur", "le", "purpl"]))