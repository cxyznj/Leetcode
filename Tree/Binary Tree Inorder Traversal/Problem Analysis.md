# [LeetCode]1.Trees and Graphs - Binary Tree Inorder Traversal

*Author：AngusChen*

## 1.问题描述
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]

> ​    1
>
> ​        ​\
>
> ​            ​2
>
> ​        /
>
> ​    3

Output: [1,3,2]

Follow up: Recursive solution is trivial, could you do it iteratively?

## 2.问题分析

（1）输入输出规定

原题目要求输入和输出都以数组形式表现，但笔者不清楚Leetcode上输入的具体方式，因此首先在输入和输出上做了一些改动：

Input: 输入n个整数及若干"#"号。输入以前序顺序给出的树中各个结点的value值，输入值为"#"代表该分支的树建立过程结束。

Output: 输出n个整数，代表树的中序遍历结果。

Example: 

input: 3 2 # 5 # # 1 # #

>​            3
>
>​        /        \
>
>​    2                1
>
>​        \
>
>​            5

output: 2 5 3 1

（2）建立二叉树

作为“树与图”板块中的第一篇内容，有必要介绍根据输入建立一棵二叉树的基本思路，在此以前序建立二叉树为例。建树的过程是一个递归的过程，首先将当前的有效输入作为（当前）根节点的value值，然后递归建立左子树、右子树。当输入无效输入（一般为#)时，结束树的该分支的建立过程，将当前结点设为空（NULL)。

```C++
// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class BinaryTree {
public:
    BinaryTree() : rootnode(NULL) {}
    ~BinaryTree() { // 收回树申请的空间，这里省略实现
    }
    void Buildtree(); // 根据用户输入建树
private:
    struct TreeNode* Buildtree_private();
    struct TreeNode* rootnode;
}

void BinaryTree:Buildtree() {
    rootnode = Buildtree_private();
}

struct TreeNode* BinaryTree:Buildtree_private() {
    struct TreeNode* tn = NULL;
    int val;
    scanf("%d", val);
    // 当输入不为#时
    if(strcmp((char)val, "#") != 0) {
        tn = new struct TreeNode(val);
        tn.left = Buildtree_private();
        tn.right = Buildtree_private();
    }
    return tn;
}
```



（3）递归实现解题思路

二叉树的前序遍历、中序遍历和后序遍历是图问题中的基础问题。我先带大家简单回顾一下二叉树前序遍历、中序遍历和后序遍历的定义：

> 前序遍历：首先访问根结点，然后遍历左子树，最后遍历右子树。在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。

> 中序遍历：首先遍历左子树，然后访问根结点，最后遍历右子树。在遍历左、右子树时，仍按照这个顺序进行。

> 后序遍历：首先遍历左子树，然后遍历右子树，最后访问根结点。在遍历左、右子树时，仍按照这个顺序进行。

采用递归方法实现二叉树的中序遍历十分简单，接下来直接用代码进行展示：

```c++
vector<int> BianryTree:inorderTraversal() {
    return inorderTraversal_private(rootnode);
}

vector<int> BianryTree:inorderTraversal_private(struct TreeNode* cnode) {
    vector<int> cv;
    cv.vector();
    vector<int>::interator cit = cv.begin();
    // 递归遍历左子树
    if(cnode->left != NULL) {
        vector<int> lv = inorderTraversal_private(cnode->left);
        cv.insert(cit, lv.begin(), lv.end());
    }
    // 将（当前）根节点加入vector中
    cv.push_back(cnode->val);
    // 递归遍历右子树
    if(cnode->right != NULL) {
        cit = cv.end();
        vector<int> rv = inorderTraversal_private(cnode->right);
        cv.insert(cit, rv.begin(), lv.end());
    }
    return cv;
}
```

(4) 迭代实现解题思路

将一个递归的过程改为迭代的过程，我通常的思路是采用栈这个数据结构作为辅助。递归的过程其实是在程序中隐式地用栈作为辅助的手段，我们只需要将这个隐式的过程显式表现出来即可。

在此题中我们需要实现的是二叉树的中序遍历。在中序遍历中，首先遍历（当前）根节点的左子树，然后遍历根节点，最后遍历根节点的右子树。在遍历中，若当前结点不为空，将当前节点压入栈中，然后将当前结点指向左子树。若当前结点为空，从栈中取出一个结点，将其加入输入序列，再将当前结点指向右子树的根节点。下面用代码展示这种思路：

```c++
vector<int> BianryTree:inorderTraversal() {
    vector<int> cv;
    cv.vector();
    if(rootnode == NULL)
        return cv;
    struct TreeNode* cnode = rootnode;
    stack<struct TreeNode*> st;
    
    while(cnode != NULL || !st.empty()) {
        if(cnode != NULL) {
            st.push(cnode);
            cnode = cnode->left;
        }
        else {
            cnode = st.top();
            st.pop();
    		cv.push_back(cnode->val);
            cnode = cnode->right;
        }
    }
    return cv;
}
```

## 3. 拓展思考

实现了迭代形式的二叉树的中序遍历，我们仍可思考前序遍历、后续遍历的迭代实现方式。在此仅给出一些思路。

（1）迭代形式的二叉树的前序遍历

二叉树的前序遍历的解题思路和中序遍历类似。首先将根节点压入栈中。在每次迭代的过程中，首先从栈中取出一个结点，将其加入输出序列，然后将右、左子树的根节点依次压入栈中（栈的“先进后出”特性），重复这个过程直到栈为空，即可实现二叉树的前序遍历。

（2）迭代形式的二叉树的后序遍历

这里给出一个巧妙的思路来实现二叉树的后序遍历，个人认为这也是最能模拟递归调用使用栈的一个过程。在二叉树的前序遍历中，调换子树根节点压栈的顺序，即将左、右子树的根节点依次压入栈中。此时遍历的顺序为“中、右、左”，遍历结束后，将输入序列进行一次reverse操作，即可将遍历的顺序调换为“左、右、中”的后序遍历顺序。

## 4. 致谢

本文中部分解题思路借鉴自”二叉树前序、中序、后序遍历的迭代实现https://www.jianshu.com/p/e0a8bbee76a9”。





