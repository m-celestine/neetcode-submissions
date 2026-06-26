class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # store results
        res = []

        # dfs back track
        def dfs(i, cur_vals, total):
            # total found
            if total == target:
                res.append(cur_vals.copy())
                return
            # base case 
            if i >= len(nums) or total > target:
                return

            # include nums[i]
            cur_vals.append(nums[i])
            dfs(i, cur_vals, total + nums[i])

            # exclude nums[i], move to next num(num[i+1])
            cur_vals.pop()
            dfs(i + 1, cur_vals, total)

        # call backtrack function
        dfs(0, [], 0)

        # return results
        return res