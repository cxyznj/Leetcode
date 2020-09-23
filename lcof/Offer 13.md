#### [剑指 Offer 13. 机器人的运动范围](https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/)

地上有一个m行n列的方格，从坐标 `[0,0]` 到坐标 `[m-1,n-1]` 。一个机器人从坐标 `[0, 0] `的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

**示例 1：**

```
输入：m = 2, n = 3, k = 1
输出：3
```

**示例 2：**

```
输入：m = 3, n = 1, k = 0
输出：1
```



**解答：**

```cpp
class Solution {
public:
    int movingCount(int m, int n, int k) {
        vector<vector<bool>> visited;
        for(int i = 0; i < m; i++) {
            vector<bool> v(n, false);
            visited.push_back(v);
        }
        return bfs(0, 0, k, m, n, visited);
    }
private:
    int bfs(int x, int y, int k, int m, int n, vector<vector<bool>>& visited) {
        if(x >= m || y >= n || visited[x][y] || sizeCount(x, y) > k) {
            return 0;
        }
        visited[x][y] = true;
        return 1 + bfs(x+1, y, k, m, n, visited) + bfs(x, y+1, k, m, n, visited);
    }

    int sizeCount(int x, int y) {
        int res = 0;
        while(x > 0) {
            res += x % 10;
            x /= 10;
        }
        while(y > 0) {
            res += y % 10;
            y /= 10;
        }
        return res;
    }
};
```



**思路：**

遇到图遍历的问题首先需要想到dfs或bfs，这里使用dfs的思路来解决遍历问题。使用bool 类型的visited二维数组来避免重复访问同一个结点。这里的一个小trick是深度遍历时只需要向右下遍历即可。