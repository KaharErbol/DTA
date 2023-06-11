def longest_substring_without_repeating(s):
    char_set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r-l+1)
    
    return res

s = "abcabcbb"
print("Result: ", longest_substring_without_repeating(s))