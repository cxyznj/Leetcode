# 11. Container With Most Water

The key thinking of this problem is "The container's height depends on the shorter side". For example, considering (i, j) represents a container which  i less than j. If the side height[i] less than height[j]. Then this container's height is depended on the left side because it is shorter. When fix the left index i and move the right index to the left, the container's height will not higher than height[i] (May shorter). Futhermore, the bottom length is shorter. Therefore we could get rid of considering about (i, i+1 to j) and know that it maximum volume is height[i] * (j - i). Then move i to the right step one. Same in other situation.



