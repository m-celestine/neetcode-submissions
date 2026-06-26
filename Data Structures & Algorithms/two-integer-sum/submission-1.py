class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list to store pair that equal the target
        storage = {}    # val : index
        
        # i go through list 1 by 1
        for index, num in enumerate(nums):
            #get diff of target an current number
            diff = target - num

            #check if diff is in dictionary storage
            if diff in storage:
                # return index of diff number , and index
                return [storage[diff], index]
            
            # store current index and number in storage
            storage[num] = index

            
        # return empty list
        return []
