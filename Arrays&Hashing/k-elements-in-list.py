from collections import Counter 
nums = [1,2]
k = 2
res = []

nums_hash = Counter(nums)

for key, value in nums_hash.items():
    if value - k >= 0:
        res.append(key)
    
print(nums_hash)
print(res, list(set(res)))