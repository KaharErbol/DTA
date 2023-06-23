def all_construct(target, wordBank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]

    for i in range(len(target) + 1):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                combo = [[*subArr, word] for subArr in table[i]]
                table[i + len(word)] += combo

    return table[len(target)]


"""
Exponential Complexity
"""

print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))