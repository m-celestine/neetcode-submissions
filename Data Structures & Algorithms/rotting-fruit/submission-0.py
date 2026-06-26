from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # get length of rows and columns
        rows, cols = len(grid), len(grid[0])

        #initialize queue, and fruit tracker
        queue = deque()
        fruits = 0

        # get position of all rotten fruits and number of fresh fruits
        for row in range(rows):
            for col in range(cols):
                # count fruit
                if grid[row][col] == 1:
                    fruits += 1
                # save position of rotten fruits
                if grid[row][col] == 2:
                    queue.append((row, col))


        # initialize time and directions
        time = 0
        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        # BFS
        while queue and fruits > 0:
            # get len of current group
            group = len(queue)
            #  traverse current group of bananas
            for _ in range(group):
                # get row and col from queue
                r, c = queue.popleft()

                # get directions
                for dr, dc in directions:
                    # get neighbors of fruit
                    row, col = r + dr, c + dc

                    # edge case
                    if (row >= 0 and row < rows) and (col >= 0 and col < cols) and grid[row][col] == 1:
                        # update fresh fruit to rotten
                        grid[row][col] = 2
                        # add position to queue
                        queue.append((row, col))
                        # decrement smount of fresh fruit
                        fruits -= 1
                    
            # increment time 
            time += 1

        # return time
        return time if fruits == 0 else -1
                    
                    

