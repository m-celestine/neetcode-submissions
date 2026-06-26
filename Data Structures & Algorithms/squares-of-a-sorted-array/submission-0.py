class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # square array
        for i, num in enumerate(nums):
            nums[i] = num * num

        # sort array
        sorted_nums = sorted(nums)

        return sorted_nums