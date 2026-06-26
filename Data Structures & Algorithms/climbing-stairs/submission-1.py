class Solution:
    def climbStairs(self, n: int) -> int:
        # Initialize the first two "ways" (like Fibonacci base cases)
        one, two = 1, 1
        
        # Loop through n-1 times (since base case already covers step 1)
        for i in range(n - 1):
            # Save the previous value of 'one'
            tmp = one
            # Update 'one' to be the sum of the last two values
            one = one + two
            # Shift 'two' forward (old 'one')
            two = tmp

        # 'one' now holds the total number of ways to climb n stairs
        return one