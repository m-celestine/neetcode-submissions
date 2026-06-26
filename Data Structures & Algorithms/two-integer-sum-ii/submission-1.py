class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # init l and r pointers
        l, r = 0, len(numbers) - 1

        while l < r:
            # update curSUm
            curSum = numbers[l] + numbers[r]
            
            # equal case
            if curSum == target:
                # return indices/positions(idx + 1)
                return [l + 1, r + 1]

            # less than case
            elif curSum < target:
                # increment left pointer
                l += 1

            # greater than case
            else:
                # increment right pointer
                r -= 1


        return []