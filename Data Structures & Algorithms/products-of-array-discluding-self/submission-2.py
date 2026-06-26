class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init prefix and postfix product arrays
        res = [1] * len(nums)

        # get prefix product of all in nums
        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # init postfix product arrays
        postfix = 1
        # get prefix product of all in nums
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i] 

        # return result array
        return res
        