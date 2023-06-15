
def grid_traveler(m,n, memo = {}): # We can pass a key word arg here
    key = (m,n)
    if key in memo: return memo[key]
    if m == 0 or n == 0: return 0
    if m == 1 and n == 1: return 1
    memo[key] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[key]

res = grid_traveler(18,18)
print(res)
    
