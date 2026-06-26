#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        // init global and curr  max and min
        int globMax = nums[0], globMin = nums[0];
        int curMax = 0, curMin = 0;

        // init total
        int total = 0;

        // kadane's variation
        for (int num = 0; num < nums.size(); num++){
            // compare and update current Max and Min
            curMax = max(curMax + nums[num], nums[num]);
            curMin = min(curMin + nums[num], nums[num]);

            // update total
            total += nums[num];

            // compare and update global Max and Min
            globMax = max(globMax, curMax);
            globMin = min(globMin, curMin);
        }

        // return statements
        if (globMax > 0){
            return max(globMax, total - globMin);
        }
        else{
            return globMax;
        }
    }
};