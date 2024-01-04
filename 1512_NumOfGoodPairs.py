from collections import Counter

nums = [1,2,3,1,1,3]

count = Counter(nums)
res = 0
for n,c in count.items():
  res += c * (c-1) // 2

print(res)


def numIdenticalPairs(nums):
    hash_table = {}
    res = 0

    for num in nums:
        if num not in hash_table:
            hash_table[num] = 0
        hash_table[num] += 1

    for val in hash_table.values():
        res += val * (val - 1) // 2

    return res