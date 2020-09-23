#### [剑指 Offer 04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

 

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。



**解答：**

```cpp
class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        int ledge, redge, upedge, downedge;
        ledge = 0;
        redge = matrix[0].size() - 1;
        upedge = 0;
        downedge = matrix.size() - 1;
        while(ledge <= redge && upedge <= downedge) {
            if(matrix[upedge][ledge] == target || matrix[upedge][redge] == target || matrix[downedge][ledge] == target || matrix[downedge][redge] == target) {
                return true;
            }
            if(matrix[upedge][redge] < target) {
                upedge++;
            }
            else if(matrix[upedge][redge] < target) {
                redge--;
            }
            else if(matrix[downedge][ledge] < target) {
                ledge++;
            }
            else if(matrix[downedge][ledge] > target) {
                downedge--;
            }
            else {
                break;
            }
        }
        return false;
    }
};
```



**思路：**

分治法即缩小问题规模的思路是一定要常想到的。面对这道题我用的也是缩小问题规模的思路，每次根据右上和左下的两个边界值去在上、下、左、右四个维度缩小矩阵的边界（左上和右下两个元素是决定性的，也可以使用到，不过一次可以将整个矩阵否定掉，如要查找的元素比左上角的数还小，那可以直接认定为false）。在缩小矩阵之前，去判断四个角的元素（即将被缩减删除的元素）是否是要查找的数，如果是的话即查找到。