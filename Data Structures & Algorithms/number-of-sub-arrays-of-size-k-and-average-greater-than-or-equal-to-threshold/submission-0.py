class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # init window
        window = []
        # init Left pointer for front of window
        L = 0
        # init sub-array tracker
        subArrs = 0

        # sliding window
        for R in range(len(arr)):
            # window size/bounds check
            if (R - L + 1) > k:
                # remove front num
                window.pop(0)
                # update L
                L += 1

            # get avg of current sub arrays
            curAvg = (sum(window) + arr[R]) / k

            # check if avg >= threshold
            if (R - L + 1) == k and curAvg >= threshold:
                subArrs += 1

            # update window
            window.append(arr[R])

        # return number of subarrs that Avg are >= threshold
        return subArrs
