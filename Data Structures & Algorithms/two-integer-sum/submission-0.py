class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list to store pair that equal the target
        pair = []
        
        # i go through list 1 by 1
        for i in range(0, len(nums)-1):
            
            # j traverse starting at the end moving towards i
            for j in range(i+1, len(nums)):
                # check if sum of values at positions of i and j equal the target
                if nums[i] + nums[j] == target:
                    pair.extend([i, j])

        # return pair indicies
        return pair
