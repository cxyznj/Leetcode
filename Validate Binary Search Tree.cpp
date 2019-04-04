/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
// 有机会应用二叉树的前序遍历类似的方法改写这段代码
class Solution {
public:
    bool isValidBST(struct TreeNode* root) {
        if(root != NULL)
            return ValidBST(root, MINVAL, MAXVAL, false, false);
        else
            return true;
    }
private:
    bool ValidBST(struct TreeNode* root, int minVal, int maxVal, bool minFlag, bool maxFlag) {
        // minFlag为真表示最小值已被更新过,maxFlag同理
        // 测试样例中出现许多-2147483648/2147483647这样的极限数据，这里的MINVAL、MAXVAL是理论上的极小值、极大值，但在比较过程中仍会出现与边界值相等的情况
        // 因此我们要注意的是，只有当MINVAL、MAXVAL被更新过后，才能用它来判断边界合法性。否则理论上不可能越过极小值、极大值的界。
        // 面对这种情况，如果C++的int类型能赋NULL值就会方便很多，不用设Flag值就可以解决问题。
        if(minFlag) {
            if(root->val <= minVal)
                return false;
        }
        if(maxFlag) {
            if(root->val >= maxVal)
                return false;
        }
        
        if(root->left != NULL) {
            // 递归判断边界合法性，缩小右边界，右边界已被更新过(maxFlag赋为true)
            if(!ValidBST(root->left, minVal, root->val, minFlag, true))
                return false;
        }
        
        if(root->right != NULL) {
            // 递归判断边界合法性，缩小左边界，左边界已被更新过(minFlag赋为true)
            if(!ValidBST(root->right, root->val, maxVal, true, maxFlag))
                return false;
        }
        
        return true;
    }
    // 理论上的最小/最大值
    int MINVAL = -2147483648;
    int MAXVAL = 2147483647;
};