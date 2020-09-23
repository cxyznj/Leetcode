#### [剑指 Offer 55 - II. 平衡二叉树](https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/)

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

**示例 1:**

给定二叉树 `[3,9,20,null,null,15,7]`

```
    3
   / \
  9  20
    /  \
   15   7
```

返回 `true` 。

```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
```

第一次练习：

```c++
#include <math.h>

class Solution {
public:
    bool isBalanced(TreeNode* root) {
        if(treeDeep(root) == -1) {
            return false;
        }
        return true;
    }
    int treeDeep(TreeNode* root) {
        if(root == NULL) {
            return 0;
        }
        int ldeep, rdeep;
        ldeep = treeDeep(root->left);
        rdeep = treeDeep(root->right);
        // 如果此树不平衡，则不返回深度而向上返回-1
        if(ldeep == -1 || rdeep == -1) {
            return -1;
        }
        if(abs(ldeep - rdeep) > 1) {
            return -1;
        }
        return 1 + ((ldeep > rdeep)? ldeep : rdeep);
    }
};
```

时间复杂度O(N)，空间复杂度O(N).

