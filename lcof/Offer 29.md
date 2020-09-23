#### [剑指 Offer 29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]



**解答：**

```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> v;
        if(matrix.empty() || matrix[0].empty()) {
            return v;
        }
        int length, width, istart, jstart;
        length = matrix.size();
        width = matrix[0].size();
        istart = 0; jstart = 0;
        enum State {Up, Down, Left, Right} state;
        state = Right;
        int i, j;
        while(true) {
            if(state == Right) {
                i = istart;
                for(j=jstart; j < width; j++) {
                    v.push_back(matrix[i][j]);
                }
                state = Down;
                istart += 1;
                if(istart >= length) {
                    break;
                }
            }
            else if(state == Down) {
                j = width-1;
                for(i=istart; i < length; i++) {
                    v.push_back(matrix[i][j]);
                }
                state = Left;
                width -= 1;
                if(jstart >= width) {
                    break;
                }
            }
            else if(state == Left) {
                i = length - 1;
                for(j=width-1; j>=jstart; j--) {
                    v.push_back(matrix[i][j]);
                }
                state = Up;
                length -= 1;
                if(istart >= length) {
                    break;
                }
            }
            else {
                j = jstart;
                for(i=length-1; i>=istart; i--) {
                    v.push_back(matrix[i][j]);
                }
                state = Right;
                jstart += 1;
                if(jstart >= width) {
                    break;
                }
            }
        }
        return v;
    }
};
```



**思路：**

这个遍历的顺序是按一定次序变化的，因此可以使用enum枚举一系列状态来依次变化。每次遍历后，改变边界的大小，使得矩阵从外至内依次遍历。由于不同遍历模式下循环的终止条件是不同的，因此只能在每次遍历结束后改变当前边界状态和遍历模式，之后分别判断是否满足终止条件。