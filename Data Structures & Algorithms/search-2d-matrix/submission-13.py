class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # get length of rows and cols
        Rows, Cols = len(matrix), len(matrix[0])

        """                 Find row                    """
        #initialize pointers for rows
        top, bot = 0, Rows - 1

        while top <= bot:
            # get middle pointer
            row = (top + bot) // 2

            # target lower than current row
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break

        
        """                 Find target                    """
        # edge case if desired row is not found
        if not (top <= bot):
            return False

        #update row to desired row
        row = (top + bot) // 2

        #initialize pointers for columns
        l, r = 0, Cols - 1

        while l <= r:
            # initialized mid pointer 
            mid = (l + r) // 2

            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True

        return False