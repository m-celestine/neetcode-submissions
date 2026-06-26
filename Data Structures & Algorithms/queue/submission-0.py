class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return self.head == None
    

    def append(self, value: int) -> None:
        #initialize new pointer
        new_node = ListNode(value)
        # check if queue empty
        if not self.tail:
            self.head = new_node
            self.tail = new_node

        else:
            #connect nodes
            new_node.prev = self.tail
            self.tail.next = new_node
            #update tail
            self.tail = new_node


    def appendleft(self, value: int) -> None:
        #initialize new pointer
        new_node = ListNode(value)
        #check if queue empty
        if not self.head:
            self.head = new_node
            self.tail = new_node
        
        else:
            #connect nodes
            new_node.next = self.head
            self.head.prev = new_node
            #update head
            self.head = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        # store value to be pop
        pop_val = self.tail.val

        # Handle case of single element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            # Update head and delink Node
            self.tail = self.tail.prev
            self.tail.next = None
        
        return pop_val
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        # store value to be pop
        pop_val = self.head.val

        # Handle case of single element
        if self.head == self.tail:
            self.head = None
            self.tail = None
        
        else:
            # Update head and delink Node
            self.head = self.head.next
            self.head.prev = None
        
        return pop_val
        
