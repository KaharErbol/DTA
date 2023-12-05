def calculateTime(self, keyboard: str, word: str) -> int:
    total = 0
    table = {keyboard[idx]: idx for idx in range(len(keyboard))}

    prev = 0
    steps = 0

    for i in range(len(word)):
        curr = word[i]
        steps += abs(table[curr] - prev)
        prev = table[curr]

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