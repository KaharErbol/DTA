def can_construct(target, wordBank):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target)+1):
        if table[i]:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] = True

    return table[len(target)]


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))


"""
a   b   c   d   e   f
0   1   2   3   4   5   6
T   F   T   T   T   T   T
            i           
"""