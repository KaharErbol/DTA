# Counting the odd letters

def longestPlaindrome(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1
    
    if odd_count <= 1:
        return len(s)
    else:
        return len(s) - odd_count + 1
    
# Counting the even letters then if there is any odd, add 1 to the result

def longestPlaindrome_2(s):
    letters = set()
    counter = 0

    for each in s:
        if each not in letters:
            letters.add(each)
        else:
            counter += 1
            letters.remove(each)

        counter = counter * 2

        if len(letters) > 0:
            counter += 1
        return counter