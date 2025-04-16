class Solution:
    def singleNumber(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return list(seen)[0]