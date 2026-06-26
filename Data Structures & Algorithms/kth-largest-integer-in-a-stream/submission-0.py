import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # keep only kth largest values (initially)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # heappop when length exceeds k
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # return kth largest val (smallest of kth largsest values)
        return self.heap[0]
