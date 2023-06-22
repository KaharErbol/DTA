def count_construct(target, wordBank):
    table = [0] * (len(target) + 1)
    table[0] = 1

    for i in range(len(target)+1):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                table[i + len(word)] += table[i]

    return table[len(target)]


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))


"""
a   b   c   d   e   f
0   1   2   3   4   5   6
1   0   1   1   2   0   1
                i                                  
"""