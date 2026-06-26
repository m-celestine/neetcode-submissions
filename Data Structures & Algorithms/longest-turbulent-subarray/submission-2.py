class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # init left and right pointers
        l, r = 0, 1
        # init result turb and prev comparison sign
        maxTurb, prev = 1, ""
        
        # get turb
        while r < len(arr):
            # less than case
            if arr[r - 1] > arr[r] and prev != ">":
                # compare max turb, l represent start of turb
                maxTurb = max(maxTurb, (r - l) + 1)
                r += 1      # increment r
                prev = ">"

            # greater than case
            elif arr[r - 1] < arr[r] and prev != "<":
                # compare max turb, l represent start of turb
                maxTurb = max(maxTurb, (r - l) + 1)
                r += 1      # increment r
                prev = "<"

            # else case
            else:
                # if prev "==" each other, reassign r -> r + 1 
                r = r + 1 if arr[r] == arr[r - 1] else r
                # reassign l 
                l = r - 1
                prev = ""

        # return max Turbulent
        return maxTurb