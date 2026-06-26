class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize sums
        maxSum = nums[0]
        curSum = 0

        # Kadanes Alg 
        for num in nums:
            # check if cur sum valid
            curSum = max(curSum, 0)
            # add num to current Sum
            curSum += num
            # compare max and curr sums
            maxSum = max(maxSum, curSum)

        # return largest sum
        return maxSum