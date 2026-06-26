class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # intialize globals and current Max and Mins
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        # init total
        total = 0
        
        # kadane's variation
        for num in nums:
            # get current Max and Min
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            # update total
            total += num
            # get current Max and Min
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)

        # return statement
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax

        """
        if globalMax > 0:
            return max(globalMax, total - globalMin)
        else:
            return globalMax
        """