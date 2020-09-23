#### [剑指 Offer 12. 矩阵中的路径](https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/)

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","**b**","c","e"],
["s","**f**","**c**","s"],
["a","d","**e**","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

**示例 ：**

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
```



**解答：**

```cpp
class Solution {
private:
    enum Direction {None, Up, Down, Left, Right};    
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(word.size() <= 0) {
            return false;
        }
        string stepword = word.substr(1);
        for(int i = 0; i < board.size(); i++) {
            for(int j = 0; j < board[0].size(); j++) {
                if(board[i][j] == word[0]) {          
                    char tmp = board[i][j];
                    board[i][j] = '\0';
                    bool stepresult = search(board, stepword, i, j, None);
                    if(stepresult) {
                        return true;
                    }
                    board[i][j] = tmp;
                }
            }
        }
        return false;
    }

    bool search(vector<vector<char>>& board, string word, int i, int j, Direction d) {
        if(word.size() <= 0) {
            return true;
        }
        char tmp;
        string searchword = word.substr(1);
        // up
        if(d != Up && i > 0 && word[0] == board[i-1][j]) {
            tmp = board[i-1][j];
            board[i-1][j] = '\0';
            if(search(board, searchword, i-1, j, Down)) {
                return true;
            }
            board[i-1][j] = tmp;
        }
        // down
        if(d != Down && i < board.size() - 1 && word[0] == board[i+1][j]) {
            tmp = board[i+1][j];
            board[i+1][j] = '\0';
            if(search(board, searchword, i+1, j, Up)) {
                return true;
            }
            board[i+1][j] = tmp;
        }
        // left
        if(d != Left && j > 0 && word[0] == board[i][j-1]) {
            tmp = board[i][j-1];
            board[i][j-1] = '\0';
            if(search(board, searchword, i, j-1, Right)) {
                return true;
            }
            board[i][j-1] = tmp;
        }
        // right
        if(d != Right && j < board[0].size() - 1 && word[0] == board[i][j+1]) {
            tmp = board[i][j+1];
            board[i][j+1] = '\0';
            if(search(board, searchword, i, j+1, Left)) {
                return true;
            }
            board[i][j+1] = tmp;
        }
        return false;
    }
};
```



**思路：**

这道题使用dfs进行的深度优先搜索框架进行搜索，时间复杂度是O(3^k * M * N)，一共M*N个可选起点，k为字符串长度，每个点平均有3个方向可以搜索（不包含走回头路的情况）。一个小trick是当一个字符匹配，切割匹配字符串为k-1（k为当前字符串长度），将棋盘的当前字符标为一个空值，执行dfs后再在棋盘上还原原字符，这样可以达到空间复杂度O（1）。