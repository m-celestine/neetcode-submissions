from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.cache:
            # Move key to end (most recently used)
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update existing key
            self.cache[key] = value
            # Move to end (most recently used)
            self.queue.remove(key)
            self.queue.append(key)
        else:
            # Add new key
            if len(self.cache) >= self.capacity:
                # Remove least recently used
                oldest_key = self.queue.popleft()
                del self.cache[oldest_key]

            self.cache[key] = value
            self.queue.append(key)