import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # make heap
        heap = nums
        heapq.heapify(heap)

        # get k largest nums
        k_large = heapq.nlargest(k, heap)

        #return kth largest val
        return k_large[-1]