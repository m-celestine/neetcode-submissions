class Solution:
    def rob(self, nums: List[int]) -> int:
        #
        rob1, rob2 = 0, 0

        #
        for num in nums:
            # get the max house
            tmp = max(num + rob1, rob2)
            # update rob1 to rob2
            rob1 = rob2
            # update rob2 to temp
            rob2 = tmp
        
        # return rob2
        return rob2

        