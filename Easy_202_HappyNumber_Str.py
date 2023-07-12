def isHappy(n):
    hash_set = set()
    while n != 1:
        if n in hash_set: 
            return False
        hash_set.add(n)
        temp_sum = 0
        for each in str(n):
            temp_sum += int(each) ** 2
        n = temp_sum
    return True