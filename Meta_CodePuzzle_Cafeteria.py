import math

def get_max_additional_diners_count(N, K, M, S):
    S.sort()
    guests = 0
    start = 1
    range_val = 0
    for seated_diner in S:
        range_val = seated_diner - start
        guests += math.floor(range_val / (K + 1))
        start = seated_diner + K + 1
    range_val = N - start + 1
    guests += math.ceil(range_val / (K + 1))

    return guests


# Example usage:

N = 10
K = 1
M = 2
S = [2, 6]

# N = 15
# K = 2
# M = 3
# S = [11, 6, 14]

max_additional_diners = get_max_additional_diners_count(N, K, M, S)

print(max_additional_diners)
