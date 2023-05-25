def add_binary(a,b):
    a_decimal = binary_to_decimal(a)
    b_decimal = binary_to_decimal(b)

    sum_decimal = a_decimal + b_decimal

    return decimal_to_binary(sum_decimal)


def binary_to_decimal(s):
    decimal = 0
    for i in range(len(s)):
        num = int(s[i])
        power = len(s) - 1 - i
        decimal += 2**power * num
    return decimal

def decimal_to_binary(decimal):
    if decimal == 0:
        return "0"
    binary = ""
    while decimal != 0:
        binary += str(decimal % 2)
        decimal = decimal // 2
    return binary[::-1]

a = "1010"
b = "1011"

print(add_binary(a, b))