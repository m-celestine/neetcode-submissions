# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:     # pairs is a list   -> return type is list of lists
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        # result:List to return, add current order of pairs
        result = [pairs[:]]

        # check if empty
        if not pairs:
            return pairs

        # go through the list of keys
        for i in range(1, len(pairs)):
            # initialize j for comparisons and traversing
            j = i-1
            
            # if value of position i is less than prev values, 
            while j >= 0 and pairs[j].key > pairs[j+1].key:
                #swap
                temp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = temp
                #decrement
                j -= 1

            # append current order of pairs to list result
            result.append(pairs[:])
        
        # return changing and sorted pairs
        return result