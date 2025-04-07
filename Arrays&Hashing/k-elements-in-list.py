from collections import Counter 
nums = [1,2,2,3,3,3]
k = 2
res = []

nums_hash = Counter(nums)
    
print(nums_hash)
print(list(nums_hash.keys()))