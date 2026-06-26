class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # init left and right pointer    
        l = 1

        for r in range(1, len(nums)):
            # different case
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        
        return l