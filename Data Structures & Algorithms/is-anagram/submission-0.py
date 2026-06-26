from collections import Counter
class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
       count_s = Counter(s)
       count_t = Counter(t)

       check = count_s == count_t

       return check