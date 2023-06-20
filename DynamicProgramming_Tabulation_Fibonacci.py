def fib(n):
    table = [0] * (n + 1)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        if (i+2) <= n:
            table[i+2] += table[i]
    return f"""
    {n}th fib num is: {table[n]}. 
    The whole list is: {table}    
    """

print(fib(6))

