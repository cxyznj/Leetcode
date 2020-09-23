#### [剑指 Offer 34. 二叉树中和为某一值的路径

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

**示例:**
给定如下二叉树，以及目标和 `sum = 22`，

```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```

返回:

```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

**解答1：**

```c++
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<int> path;
        vector<vector<int>> paths;
        if(root) {
            paths = findPath(root, sum, path);
        }
        return paths;
    }
    vector<vector<int>> findPath(TreeNode* root, int sum, vector<int> path) {
        int curval = sum - root->val;
        path.push_back(root->val);
        vector<vector<int>> empty;
        if(curval == 0) {
            if(root->left == nullptr && root->right == nullptr) {
                empty.push_back(path);
                return empty;
            }
        }
        vector<vector<int>>::iterator it;
        if(root->left) {
            vector<vector<int>> lpath = findPath(root->left, curval, path);
            for(it = lpath.begin(); it != lpath.end(); it++) {
                empty.push_back(*it);
            }
        }
        if(root->right) {
            vector<vector<int>> rpath = findPath(root->right, curval, path);
            for(it = rpath.begin(); it != rpath.end(); it++) {
                empty.push_back(*it);
            }
        }
        return empty;
    }
};
```

时间复杂度和空间复杂度都为O(N)