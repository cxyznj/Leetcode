#### [剑指 Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

难度简单122

输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。

要求时间复杂度为O(n)。

 

**示例1:**

```
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
```



**解答：**

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.empty()) return 0;
        vector<int> dp(nums.size());
        dp[0] = nums[0];
        int max = dp[0];
        for(int i = 1; i < nums.size(); i++) {
            dp[i] = nums[i];
            if(dp[i-1] > 0) {
                dp[i] += dp[i-1];
            }
            if(dp[i] > max) {
                max = dp[i];
            }
        }
        return max;
    }
};
```



**思路：**

这是一道用动态规划思路解决的题目，对以第i个元素为结尾的子数组做动态规划，转移方程为：
$$
dp[i] = \left\{
\begin{aligned}
nums[i] & , dp[i-1] < 0 \\
nums[i] + dp[i-1] & , dp[i-1] >= 0
\end{aligned}
\right.
$$
当前方子数组最大和小于0时，以第i个元素结尾的子数组仅算它自己才是最大和，此时抛弃掉前方小于0的子数组不与其合并。

时间复杂度为O(n)，空间复杂度为O(n).