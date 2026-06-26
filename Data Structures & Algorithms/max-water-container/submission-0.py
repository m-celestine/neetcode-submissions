class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # init left and right pointers
        l, r = 0, len(heights) - 1
        #init max water
        maxWater = 0

        while l <= r:
            # get possible level for container
            level = min(heights[l], heights[r])
            # get posible water container
            maxWater = max(maxWater, (r - l) * level)

            # move left pointer
            if heights[l] <= heights[r]:
                l += 1
            # move right pointer
            elif heights[l] > heights[r]:
                r -= 1

        # return maxWater
        return maxWater