class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init prefix and postfix product arrays
        prefix = []

        # get prefix product of all in nums
        for num in nums:
            if not prefix:
                prefix.append(num)
                continue
            
            prefix.append(num * prefix[-1])

        # init postfix product arrays
        revNums = nums[-1::-1]
        postfix = []
        # get prefix product of all in nums
        for num in revNums:
            if not postfix:
                postfix.append(num)
                continue
            
            postfix.append(num * postfix[-1])

        # reverse postfix array
        postfix = postfix[-1::-1]



        # init output arr
        output = []
        
        # assign and structure output arr
        for idx in range(len(nums)):
            # beginning case
            if idx == 0:
                output.append(postfix[idx + 1])
                continue
            
            # end cases
            if idx == len(nums) - 1:
                output.append(prefix[idx - 1])
                # return list
                return output

            # get prod of all except curr num
            output.append(prefix[idx - 1] * postfix[idx + 1])

        