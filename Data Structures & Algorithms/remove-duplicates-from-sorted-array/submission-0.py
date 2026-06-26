class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # init left and right pointer    
        l = r = 1

        while r < len(nums):
            # different case
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
            r += 1
        
        return l