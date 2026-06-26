# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # result to return
        result = [pairs[:]]

        # check if empty
        if not pairs:
            return pairs

        # go through the list of keys
        for i in range(1, len(pairs)):
            # place holder for current value of position i
            curr = pairs[i]
            # initialize j for comparisons and traversing
            j = i-1
            
            # if value of position i is less than prev values, 
            while j >= 0 and pairs[j].key > curr.key:
                #shifts left bigger values to the right
                pairs[j+1] = pairs[j]
                #decrement
                j -= 1
            # place i place holder in correct position
            pairs[j+1] = curr

            # append list to list result
            result.append(pairs[:])
        
        # return sorted pairs
        return result