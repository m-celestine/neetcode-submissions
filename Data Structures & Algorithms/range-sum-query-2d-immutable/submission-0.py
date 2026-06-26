class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.preSum = matrix

        for row in range(len(matrix)):
            # reset total
            total = 0

            for col in range(len(matrix[0])):
                # update total
                total += matrix[row][col]
                # append list of sums in curr row and col
                self.preSum[row][col] = total


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # placeholder for sum
        total = 0
        # row teacker
        row = row1

        # traverse rows
        while row <= row2:
            # base case for when col1 == 0
            if col1 == 0:
                # get total 
                total += self.preSum[row][col2]
            
            else:
                total += self.preSum[row][col2] - self.preSum[row][col1 -1]
            
            row += 1


        # return total
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)