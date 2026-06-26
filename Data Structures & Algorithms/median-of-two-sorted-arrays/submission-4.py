class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            num2 = int(len(nums) / 2)
            num1 = num2 - 1

            median = (nums[num2] + nums[num1]) / 2
            return median

        num = int(len(nums) / 2)

        median = nums[num]
        return median