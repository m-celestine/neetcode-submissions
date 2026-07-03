from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get frequencies
        freqs = Counter(nums)
        #init heap and return topK lists
        heap = []
        topK = []

        #add to heap using frequency
        for key, val in freqs.items():
            #init pair for max heap
            pair = (-val, key)
            #init max heap based on freqs
            heapq.heappush(heap, pair)

        # get the top k freq from max heap
        while heap and k > 0:
            # extract values from pair
            pair = heapq.heappop(heap)
            # add key to list
            topK.append(pair[1])
            #decrement k
            k -= 1

        return topK