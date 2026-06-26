import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make custom heap using Euclidean Distance
        ed_heap = []
        for point in points:
            pair = (self.eucDist(point[0], point[1]), point)
            ed_heap.append(pair)
        
        # heapify
        heapq.heapify(ed_heap)

        # grab k closest points (smallest points)
        k_small = heapq.nsmallest(k, ed_heap)

        # get points of the k smallest
        results = []
        while k_small:
            pair = heapq.heappop(k_small)
            results.append(pair[1])

        return results


    # Euclidean Distance
    def eucDist(self, x, y):
        return math.sqrt( (x**2) + (y**2) )