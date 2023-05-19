def isAnagram(s,t):
    if len(s) == len(t):
        for each in set(t):
                if s.count(each) != t.count(each):
                    return False
        return True
    return False


# Follow up: 
# What if the inputs contain Unicode characters? 
# How would you adapt your solution to such a case?

def isAnagramUni(s, t):
        s_uni = [ord(each) for each in s]
        t_uni = [ord(each) for each in t]

        if len(s_uni) != len(t_uni):
            return False

        s_uni.sort()
        t_uni.sort()

        for i in range(len(t_uni)):
            if t_uni[i] != s_uni[i]:
                return False

        return True