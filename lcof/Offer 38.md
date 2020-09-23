#### [剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

输入一个字符串，打印出该字符串中字符的所有排列。

 

你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

 

**示例:**

```
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]
```



**解答**

```cpp
class Solution {
public:
    vector<string> permutation(string s) {
        vector<string> res;
        if(s.empty()) return res;
        dfs(0, s, res);
        return res;
    }
    void rearrange(int x, string& s, vector<string>& res) {
        if(x == s.size() - 1) {
            res.push_back(s);
        }
        set<char> pruning;
        // 将[x, s.size()-1]的字符依次放到x位
        for(int i = x; i < s.size(); i++) {
            if(pruning.find(s[i]) != pruning.end()) {
                continue;
            }
            else {
                pruning.insert(s[i]);
            }
            swapval(s, x, i);
            rearrange(x+1, s, res);
            swapval(s, x, i);
        }
    }

    void swapval(string& s, int x, int y) {
        char tmp = s[x];
        s[x] = s[y];
        s[y] = tmp;
    }
};
```



**思路：**

面对这个问题首先要明确这是一个分治问题，求长度为n的字符串的全排列=全排列第一位字符+求长度为n-1的字符串的全排列。妙点在于通过交换来确定一个位置的字符，这个交换的步骤导致被固定的字符自动不被后面的递归过程考虑到。一个关键点在于必须要通过剪枝来去除重复值（当然，放到Set中最后再转化为数组也是可以的）。这个剪枝的关键在于只有重复字符会造成重复字符串。所以在同一个位置使用Set集合来避免重复字符的重复递归。