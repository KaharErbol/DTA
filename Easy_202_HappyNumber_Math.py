def isHappy(n):
    visited = set()

    while n not in visited:
        visited.add(n)
        n = sumOfSquare(n)

        if n == 1:
            return True
        
    return False


def sumOfSquare(n):
    output = 0
    while n:
       digit = n % 10
       digit = digit ** 2
       output += digit
       n = n // 10
    
    return output


print(isHappy(255))