class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # init set tracker
        charSet = set()
        #init L pointer and length
        L = 0
        length = 0

        for R in range(len(s)):
            # repeat case
            while s[R] in charSet:
                # remove char and increment L
                charSet.remove(s[L])
                L += 1

            # add new char
            charSet.add(s[R])
            length = max(length, R - L + 1)

        # return length
        return length
        