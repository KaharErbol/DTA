import math

def get_max_additional_diners_count(N, K, M, S):
    S.sort()
    extraSpace = 0
    firstOpenSeat = 1

    for takenSeat in S:
        openSeats = takenSeat - K - firstOpenSeat
        if (openSeats > 0):
            extraSpace += math.ceil(openSeats/(K+1))
        firstOpenSeat = takenSeat + K + 1
    
    # After the right most taken seat
    openSeats = N + 1 - firstOpenSeat
    if(openSeats > 0):
        extraSpace += math.ceil(openSeats/(K+1))
    
    return extraSpace



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
