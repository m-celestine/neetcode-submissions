class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0  # Count of subarrays summing to k
        curSum = 0  # Running cumulative sum
        prefixSum = {0: 1}  # Map: cumulative_sum -> frequency. Start with {0:1} for subarrays from index 0

        for n in nums:
            curSum += n  # Add current element to cumulative sum
            diff = curSum - k  # Find what previous sum we need to form a subarray summing to k
            
            res += prefixSum.get(diff, 0)  # Add count of times we've seen that sum (those are valid subarrays)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)  # Store/update frequency of current cumulative sum

        return res


# EXAMPLE: nums = [1, 2, 3], k = 3
# 
# Start: res=0, curSum=0, prefixSum={0:1}
# 
# n=1: curSum=1, diff=-2, res+=0, prefixSum={0:1, 1:1}
# n=2: curSum=3, diff=0, res+=1 (found [1,2]), prefixSum={0:1, 1:1, 3:1}  
# n=3: curSum=6, diff=3, res+=1 (found [3]), prefixSum={0:1, 1:1, 3:1, 6:1}
# 
# Result: 2 subarrays found