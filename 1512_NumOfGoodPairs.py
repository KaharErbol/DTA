from collections import Counter

nums = [1,2,3,1,1,3]

count = Counter(nums)
res = 0
for n,c in count.items():
  res += c * (c-1) // 2

print(res)


def numIdenticalPairs(self, nums):
        hash_map = {}
        res = 0
        for element in nums:
            if element not in hash_map:
                hash_map[element] = 0
            hash_map[element] += 1
        
        for k,v in hash_map.items():
            res += v * (v - 1) // 2
    
        return res