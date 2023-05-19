def isPlaindrome(x: int) -> bool:
    x = str(x)
    return x == x[::-1]