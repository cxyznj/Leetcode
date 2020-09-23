#### [剑指 Offer 63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？

 

**示例 1:**

```
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
```

**示例 2:**

```
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```



**解答1：**

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()) {
            return 0;
        }
        // d[i]表示在第i天卖出的最大收益
        vector<int> d(prices.size());
        d[0] = 0;
        int i;
        int maxpro = 0;
        // 默认股票在第0天买入
        for(i = 1; i < prices.size(); i++) {
            // 当curpro大于0的时候，表示当前股票的价格大于买入的价格
            int curpro = d[i-1] + (prices[i] - prices[i-1]);
            // 如果d[i]被更新为0，表示当前的股票价格小于买入的价格，第i天被更新为买入日期
            d[i] = (curpro > 0)? curpro : 0;
            // 记录当前的最高利润
            maxpro = (d[i] > maxpro)? d[i] : maxpro;
        }
        return maxpro;
    }
};
```



**解答2：**

```cpp

```

