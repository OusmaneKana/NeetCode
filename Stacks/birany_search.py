class Solution:
    def search(self, nums, target):
        l, r, mid = 0, len(nums) -1, len(nums)//2

        