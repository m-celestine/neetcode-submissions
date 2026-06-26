class Solution:
    def trap(self, height: List[int]) -> int:
        # base case
        if not height:
            return 0

        # init pointers
        l = 0
        r = len(height) - 1
        
        # init left and right max
        leftMax, rightMax = height[l], height[r]
        # init result
        res = 0
        
        while l < r:
            # when leftMax is smaller than rightMax, modify left
            if leftMax < rightMax:
                # update left pointer, leftMax, and results
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            
            # when leftMax is bigger than rightMax, modify lrighteft
            else:
                # update right pointer, rightMax, and results
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
            
        # return results
        return res
