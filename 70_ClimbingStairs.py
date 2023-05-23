def climbStairs(n):
    if n <= 2:
        return n

    # create a list to store steps for each n
    steps = [0] * (n+1)
    steps[1] = 1
    steps[2] = 2

    for i in range(3, n+1):
        steps[i] = steps[i-1] + steps[i-2]

    return steps[n]


def climbStairs_2(n):
    if n <= 2:
        return n
    
    prev = 1
    nxt = 2

    for i in range(3, n+1):
        temp = prev + nxt
        prev = nxt
        nxt = temp

    return nxt