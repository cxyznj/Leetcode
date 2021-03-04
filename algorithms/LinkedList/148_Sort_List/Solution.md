# 148. Sort List

The problem is to sort the linked list in O(nlogn) time and using only constant extra space. If we look at various sorting algorithms, Merge Sort and Quick Sort are two efficient sorting algorithms. Merge Sort is more suitable in here.

Merge Sort follows the Divide and Conquer Strategy:

Divide phase: Divide the problem into subproblems.

Conquer phase: Pepeatedly solve each subproblem independently and combine the result to form the original problem.

In this problem, we divide the Linked List into until the sublist contains only one elements. And in conquer phase, link the elements in two Linked List to be merged one by one with their value. Repeat the process until the whole list is be merged.

It is very simple for array. However, finding the middle point(the spliting point) is not much obviously in linked list. Use step idea to solve it: set two pointer, first one traverse 2 steps a time and the second one traverse 1 step a time. When the first meet the end then the position of the second pointer is the middle place. 

