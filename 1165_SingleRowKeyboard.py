"""
There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25). Initially, your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

 

Example 1:

Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4. 
"""

def calculateTime(keyboard: str, word: str) -> int:
    table = {keyboard[idx]: idx for idx in range(len(keyboard))}

    steps = 0
    prev = 0

    for i in range(len(word)):
        cur = table[word[i]]
        steps += abs(cur - prev)
        prev = cur

    return steps



    


"""
   def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i
        res = 0
        temp = 0
        for c in word:
            res += abs(d[c]-temp)
            temp = d[c]
        return res
"""