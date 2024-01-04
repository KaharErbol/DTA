"""
1. Ascending Binary Sorting
Consider an array of decimal integers.
Rearrange the array according to the following rules:
*   Sort the integers in ascending order by the number of 1's in their binary representations.
*   Elements having the same number of 1's in their binary representations are ordered by increasing decimal value.
Example
Consider the array [7, 8, 6, 5]10 = [0111, 1000, 0110, 010112. First, group the items by number of binary digits equal to 1: [[1000], [0101, 0110], [0111112. The elements with two 1's now must be ordered: [0110, 010112 = [6, 5]10. Sort those two elements in ascending order by value making the final array [1000, 0101, 0110, 0111]2 =
[8, 5, 6, 7]10.
"""

def ascending_binary_sort(arr):
    # Define a custom sorting key function
    def sort_key(num):
        # Count the number of set bits (1's) in the binary representation
        count_ones = bin(num).count('1')
        # Create a tuple with count of 1's and the original number for sorting
        return (count_ones, num)

    # Sort the array using the custom key function
    sorted_arr = sorted(arr, key=sort_key)

    return sorted_arr

# Example usage
input_array = [7, 8, 6, 5]
result = ascending_binary_sort(input_array)
print(result)


print('####################################')

def is_almost_equivalent(s, t):
    if len(s) != len(t):
        return False
    
    # Count occurrences of each lowercase letter in both strings
    count_s = [0] * 26
    count_t = [0] * 26

    for char in s:
        count_s[ord(char) - ord('a')] += 1

    for char in t:
        count_t[ord(char) - ord('a')] += 1

    # Check if the counts differ by no more than 3 for each letter
    for i in range(26):
        if abs(count_s[i] - count_t[i]) > 3:
            return False

    return True

def are_almost_equivalent_pairs(s, t):
    result = []

    for pair in zip(s, t):
        is_almost_equiv = is_almost_equivalent(pair[0], pair[1])
        result.append('YES' if is_almost_equiv else 'NO')

    return result

# Example usage
s = ["abc", "xyz", "def"]
t = ["bcd", "yza", "dfe"]
result = are_almost_equivalent_pairs(s, t)
print(result)

