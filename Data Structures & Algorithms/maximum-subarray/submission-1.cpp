#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        // initialize sums
        int maxSum = nums[0];
        int curSum = 0;

        // kadane's Algorithm
        for (int num = 0; num < nums.size(); num++){
            // check if curSum is valid
            curSum = max(curSum, 0);
            // add num to current sum
            curSum += nums[num];
            // compare sums
            maxSum = max(maxSum, curSum);
        }

        // return largest sum
        return maxSum;

    }
};
