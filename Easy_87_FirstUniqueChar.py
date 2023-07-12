def first_uniq_char(s):
    st_map = {}
    for c in s:
        if c not in st_map:
            st_map[c] = True
        else:
            st_map[c] = False

    for i in range(len(s)):
        if st_map[s[i]]:
            return i
        
    return -1



print(first_uniq_char("lovegitleetcode"))