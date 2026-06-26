from collections import deque
"""             Using queues                   """
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move key to end (most recently used)
            self.cache.move_to_end(key)
            # return val of key
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:    
        if key in self.cache:
            # update position of kev-value pair
            self.cache.move_to_end(key)
        # Create/Update value at key
        self.cache[key] = value

        # capacity check
        if len(self.cache) > self.cap:
            self.cache.popitem(0)
