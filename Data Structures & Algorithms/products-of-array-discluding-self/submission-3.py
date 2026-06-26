class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init prefix and postfix product arrays
        res = [1] * len(nums)

        # init prefix product arrays
        prefix = 1
        # get prefix product of all in nums
        for i in range(len(nums)):
            res[i] = prefix     # Store product of all elements BEFORE i
            prefix *= nums[i]   # Update prefix to include nums[i]

        # init postfix product arrays
        postfix = 1
        # get prefix product of all in nums
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix    # Multiply by product of all elements AFTER i
            postfix *= nums[i]   # Update postfix to include nums[i]

        # return result array
        return res
        