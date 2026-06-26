class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # countDups hashmap to check for duplicates
        countDups = {}

        # check if number in Hash map
        for num in nums:
            # if not in hash, add it
            if num not in countDups:
                countDups[num] = 1
            # if already in hash map, returen True
            else:
                countDups[num] += 1
                return True
        
        #if nums does not have dups by the end 
        return False

            
