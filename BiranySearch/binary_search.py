class Solution:
    def search(self, nums, target: int) -> int:
        
        l,r  = 0, len(nums) -1
    
        while l<=r:
            mid = l + ((r-l) //2)
            print(mid)

            if nums[mid] > target:
                r = mid -1
            if nums[mid] < target:
                l= mid +1
            else:
                return mid
        

        return -1




nums = [-1,0,2,4,6,8]
target = 4


print("Solution", Solution().search(nums, target))