from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init counter dict
        count = defaultdict(int)
        # init length and frequency counter
        length = 0
        maxCount = 0

        # init left pointer
        l = 0

        for r in range(len(s)):
            # increment num of char in count
            count[s[r]] += 1
            # compare/reassign freq counter
            maxCount = max(maxCount, count[s[r]])

            # remove case
            while (r - l + 1) - maxCount > k:
                # remove then increment left pointer
                count[s[l]] -= 1
                l += 1
                

            # check length
            length = max(length, r - l + 1)

        # return length
        return length