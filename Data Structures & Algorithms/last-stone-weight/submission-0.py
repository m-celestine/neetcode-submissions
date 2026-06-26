import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need the two heaviest stones (max_heap)
        # negate to negative for max heap
        stones = [-stone for stone in stones]
        # heapify stones
        heapq.heapify(stones)

        # loop until one rock or non standing
        while len(stones) > 1:
            # get 2 heaviest stones
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)

        # incase stones is empty
        stones.append(0) 
        # return last stone weight
        return abs(stones[0])   # abs to negate back to positive

