class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # store results
        res = []

        # store for subsets
        subset = []

        # dfs back track
        def dfs(i):
            # base/edge case
            if i >= len(nums):
                res.append(sorted(subset))
                return

            # Decision to include the current num[i]
            subset.append(nums[i])
            dfs(i+1)

            # Decision to exclude the current num[i]
            subset.pop()
            dfs(i+1)

        
        # call dfs back track function
        dfs(0)

        # return result
        return res