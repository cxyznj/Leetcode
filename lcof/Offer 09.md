**解答1：**

```c++
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.empty()) {
            return nullptr;
        }
        TreeNode* root = new TreeNode(preorder[0]);
        int i;
        int divpoint = 0;
        for(i = 0; i < inorder.size(); i++) {
            if(inorder[i] == preorder[0]) {
                divpoint = i;
                break;
            }
        }
        vector<int> leftinorder;
        for(i = 0; i < divpoint; i++) {
            leftinorder.push_back(inorder[i]);
        }
        vector<int> rightinorder;
        for(i = divpoint + 1; i < inorder.size(); i++) {
            rightinorder.push_back(inorder[i]);
        }
        vector<int> nextpreorder;
        for(i = 1; i < preorder.size(); i++) {
            nextpreorder.push_back(preorder[i]);
        }
        root->left = buildTree(nextpreorder, leftinorder);
        root->right = buildTree(nextpreorder, rightinorder);
        return root;
    }
};
```

**解答2：**

```c++
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if(preorder.empty()) {
            return nullptr;
        }
        else if(preorder.size() == 1) {
            return new TreeNode(preorder[0]);
        }
        int scope[4] = {0};
        scope[1] = preorder.size();
        scope[3] = inorder.size();
        map<int, int> inmap;
        int i;
        for(i = 0; i < inorder.size(); i++) {
            inmap.insert(map<int, int>::value_type(inorder[i], i));
        }
        return subbuildTree(preorder, inorder, scope, inmap);
    }
    TreeNode* subbuildTree(vector<int>& preorder,vector<int>& inorder, int* scope, map<int, int> inmap){
        if(scope[1]-scope[0] <= 0) {
            return nullptr;
        }
        TreeNode* rtnode = new TreeNode(preorder[scope[0]]);
        if(scope[1]-scope[0] == 1) {
            return rtnode;
        }
        int x = preorder[scope[0]];
        int index = inmap[x];
        int leftsize = index - scope[2] - 1;
        if(leftsize < 0) leftsize = 0;
        int rightsize = scope[3] - index - 1;
        if(rightsize < 0) rightsize = 0;
        if(leftsize > 0) {
            int leftscope[4] = {0};
            leftscope[0] = scope[0] + 1;
            leftscope[1] = leftscope[0] + leftsize;
            leftscope[2] = scope[2];
            leftscope[3] = index - 1;
            rtnode->left = subbuildTree(preorder, inorder, leftscope, inmap);
        }
        if(rightsize > 0) {
            int rightscope[4] = {0};
            rightscope[0] = scope[0] + 1 + leftsize;
            rightscope[1] = scope[1];
            rightscope[2] = index + 1;
            rightscope[3] = scope[3];
            rtnode->right = subbuildTree(preorder, inorder, rightscope, inmap);
        }
        return rtnode;
    }
};
```

**思路：**

