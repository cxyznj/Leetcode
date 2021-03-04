## 28. Implement strStr

This problem can be treat as "Finding a match pattern in text" problem. And KMP algorithm is one of the best way to solve it. And the time complexity is O(m) + O(n). Where O(n) is to calculate "next" array and O(m) represent that only need to traverse the text once.



To understand that, we need know PMT(Partial Match Table). The value of PMT means the longest match length of prefix and suffix of current string. For example, consider about string "ababa", prefix is {"a", "ab", "aba", "abab"} and the suffix is {"a", "ba", "aba", "baba"}. Therefore the longest match is "aba" and the PMT value of "ababa" is 3.

![img](https://pic1.zhimg.com/80/v2-e905ece7e7d8be90afc62fe9595a9b0f_1440w.jpg?source=1940ef5c)

The first step of KMP algorithm is to calculate PMT of pattern string, and generate "next" array based on PMT —— move PMT to the right one step and fill "-1" in the 0 position of "next" array.

![img](https://pic1.zhimg.com/80/v2-40b4885aace7b31499da9b90b7c46ed3_1440w.jpg?source=1940ef5c)

Next step is to match each character of text and pattern one by one. Let us assume that there have two pointers named i and j respectively point the position of text and patter string. If two characters are match, then move the pointers of text and pattern to the right one step; While it not match, the "next" array tell us how to move j pointer. For example, if it not match when j == 4, it means pattern[j] did not match text[i] (while pattern[0:j] match text[i-j:i]). Look up table knows that next[j] == 2. It means pattern[0:j]'s longest match length of prefix and suffix is 2, the match string is "ab". We could find text[i-2:i] also "ab" because text[i-2:i] match patter[j-2:j], and from pmt we know [j-2:j] match patten[0:2]. With the transmissibility, the pattern[0:2] match text[i-2:i]. That is the key of this algorithm. In the subsequent process, compare pattern[0:2] and text[i-2:i] is already not needed. We could keep i in in the same position and move j to the 2 (the next[j] represent the position that need to move). Then continue compare text[i] and pattern[j]. next[0] == -1 just for the convience for coding.



The last question is how to generate next array with efficient. It use next array also and because generate next array is from left to the right. So we can use previous next array to reconsider current circumstance. The key idea is ***same***.

