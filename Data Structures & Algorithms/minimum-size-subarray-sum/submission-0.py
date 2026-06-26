class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # init Left pointer and sum
        L = 0
        curSum = 0
        # init length to infinity
        length = float("inf")

        # get min length subarr sum
        for R in range(len(nums)):    
            curSum += nums[R]

            while curSum >= target:
                #get length of subarr
                length = min(length, R - L + 1)
                # update L and cur sum for next num
                curSum -= nums[L]
                L += 1

        # return length
        return 0 if length == float("inf") else length
