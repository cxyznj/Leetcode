#### [剑指 Offer 55 - I. 二叉树的深度](https://leetcode-cn.com/problems/er-cha-shu-de-shen-du-lcof/)

输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。

例如：

给定二叉树 `[3,9,20,null,null,15,7]`，

```
    3
   / \
  9  20
    /  \
   15   7
```

返回它的最大深度 3 。

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
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(root == NULL)
        {
            return 0;
        }
        int deep = 1;
        int leftDeep, rightDeep, subDeep;
        leftDeep = maxDepth(root->left);
        rightDeep = maxDepth(root->right);
        subDeep = (leftDeep > rightDeep)? leftDeep : rightDeep;
        return deep + subDeep;
    }
};
```

这是一种基于DFS的后序遍历解题方法。



第二次练习：

```c++
#include <queue>
using namespace std;

class Solution {
public:
    int maxDepth(TreeNode* root) {
        int deep = 0;
        queue<struct TreeNode*> q;
        q.push(root);
        while(q.size() > 0)
        {
            queue<struct TreeNode*> tmp;
            while(q.size() > 0)
            {
                struct TreeNode* node;
                node = q.front();
                q.pop();
                if(node != NULL)
                {
                    tmp.push(node->left);
                    tmp.push(node->right);
                }
            }
            if(tmp.size() > 0)
            {
                q = tmp;
                deep += 1;
            }
        }
        return deep;
    }
};
```



