class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        s = s.lower()

        while L < R:
            # make sure left pointer is valid
            while L < R and not s[L].isalnum():
                L += 1
            # make sure right pointer is valid
            while L < R and not s[R].isalnum():
                R -= 1

            # False case
            if s[L] != s[R]:
                return False

            # Increment L, Decrement R
            L += 1
            R -= 1

        # return True
        return True