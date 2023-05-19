def romanToInt(s: str) -> int:
        roman_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        if len(s) == 1:
            return roman_int[s]

        s = s.replace("IV","IIII").replace("IX","VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        result = 0
        for each in s:
            result += roman_int[each]
        return result

## solution 2
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        }
    
        result = 0
        prev = 0
        for char in s[::-1]:
            curr = roman_int[char]
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr
        
        return result