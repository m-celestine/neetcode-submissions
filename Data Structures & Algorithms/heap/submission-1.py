class MinHeap:
    
    def __init__(self):
        self.heap = [0]


    def push(self, val: int) -> None:
        # append val to heap
        self.heap.append(val)

        # get index of new val
        index = len(self.heap) - 1

        # Perculate Up
        self.bubble_up(index)

        return


    def pop(self) -> int:
        # base case - check if heap has actual elements beyond dummy node
        if len(self.heap) <= 1:
            return -1

        # single value case
        if len(self.heap) == 2:
            return self.heap.pop()

        # get smallest val (top val)
        min_val = self.heap[1]

        # update top of heap with end
        self.heap[1] = self.heap.pop()

        # index for val
        i = 1

        # Perculate Down
        self.bubble_down(i)

        # return popped val
        return min_val
        

    def top(self) -> int:
        # base case
        if len(self.heap) <= 1:
            return -1
        
        # return top val
        return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        # add nums to heap ( dummy node + nums(list))
        self.heap = [0] + nums[:]

        # get last parent index (with Children {(n-1)//2})
        cur = (len(self.heap) - 1) // 2

        # move from lowest parent up to highest parent(top)
        while cur > 0:
            # Perculate Down
            self.bubble_down(cur)

            # Decrement current
            cur -= 1

        
        
    def bubble_up(self, val_index):
        # get parent index
        parent = val_index // 2

        """         Perculate Ip            """
        # position val into correct position
        while (val_index > 1) and (self.heap[val_index] < self.heap[parent]):
            
            # swap parent and curr index
            self.heap[val_index], self.heap[parent] = self.heap[parent], self.heap[val_index]
            
            # update index of new val
            val_index = parent
            # update parent
            parent = val_index // 2

    def bubble_down(self, index):
        
        """         Perculate Down            """
        while index * 2 < len(self.heap):
            # store index of left and right child
            left_child = index * 2
            right_child = index * 2 + 1

            # check if right child exists and is smaller than both parent and left child
            if right_child < len(self.heap) and self.heap[right_child] < self.heap[index] and self.heap[right_child] < self.heap[left_child]:
                # swap right child with current(parent)
                self.heap[right_child], self.heap[index] = self.heap[index], self.heap[right_child]
                # update index
                index = right_child

            # check if left child is smaller than parent
            elif left_child < len(self.heap) and self.heap[left_child] < self.heap[index]:
                # swap left child with current(parent)
                self.heap[left_child], self.heap[index] = self.heap[index], self.heap[left_child]
                # update index
                index = left_child

            # break loop
            else:
                break
        
        