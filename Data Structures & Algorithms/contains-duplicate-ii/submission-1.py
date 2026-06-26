class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # init window hashset
        window = set()
        # init Left pointer
        L = 0

        for R in range(len(nums)):
            # check if Left pointer out of bounds
            if R - L > k:
                # remove the current front of window
                window.remove(nums[L])
                # slide our left over, shift window over
                L += 1

            # check if R is in our window
            if nums[R] in window:
                return True
            
            # add current R to our window
            window.add(nums[R])

        # return False if loop exited
        return False
