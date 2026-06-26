class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # init slow and fast pointers
        slow = fast = 0
        # get length of array
        n = len(nums)

        while slow != n:
            # move pointers
            slow += 1
            fast += 2

            # check if match 
            if nums[slow] == nums[0] or nums[fast] == nums[0] and (slow and fast) != 0 :
                return nums[0]
            
            elif nums[slow] == nums[fast] and slow != fast:
                return nums[slow]

            if fast >= n - 2:
                fast = 1


            