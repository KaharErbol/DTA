def canConstruct_1(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    
    for each in ransomNote:
        if each in magazine:
            magazine = magazine.replace(each, "", 1)
        else:
            return False
    
    return True

def canConstruct_2(ransomNote, magazine):
    ransom_count = {}
    mag_count = {}

    for each in ransomNote:
        if each not in ransom_count:
            ransom_count[each] = 0
        ransom_count[each] += 1

    for each in magazine:
        if each not in mag_count:
            mag_count[each] = 0
        mag_count[each] += 1
    
    for char, count in ransom_count.items():
        if count > mag_count.get(char, 0):
            return False

    return True
            