class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # init sub-array tracker
        subArrs = 0
        # curSum tracker
        curSum = sum(arr[:k-1]) # non inclusive

        # sliding window
        for L in range(len(arr) - k + 1):
            # add end of window (R) to curSum
            curSum += arr[L + k - 1]

            # check if avg >= threshold
            if (curSum / k) >= threshold:
                subArrs += 1
            
            # decremtent curSum by removing beginning of window
            curSum -= arr[L]

        # return number of subarrs that Avg are >= threshold
        return subArrs
