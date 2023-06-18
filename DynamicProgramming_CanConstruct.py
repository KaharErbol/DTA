"""
Return boolean indicating if the target can be 
constructed by concatenating the elements of wordBank.
Elements can be used as many times as needed.
"""
def can_construct(target, wordBank, memo={}):
    if target in memo: return memo[target]
    if target == "": return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]
            if can_construct(suffix, wordBank, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    return False

print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
