class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.cap = capacity
        self.length = 0


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        if self.array[i] == 0:
            self.length += 1

        self.array[i] = n


    def pushback(self, n: int) -> None:
        if self.length >= self.cap:
            self.resize()

        self.array[self.length] = n
        self.length += 1


    def popback(self) -> int:
        temp = self.array[self.length - 1]   # copy value
        self.array[self.length - 1] = 0      # remove value from array
        self.length -= 1        # update length
        return temp             # return popped value
 

    def resize(self) -> None:
        new_array = [0] * (self.cap * 2)

        for idx in range(self.cap):
            new_array[idx] = self.array[idx]

        self.array = new_array
        self.cap = self.cap * 2


    def getSize(self) -> int:
        return self.length
        
    
    def getCapacity(self) -> int:
        return self.cap
