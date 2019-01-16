||Singly Linked List Set|Binary Search Tree Set|
|----|----|----|
|增add|O(n)|O(h)|
|查contains|O(n)|O(h)|
|删remove|O(n)|O(h)|

h为二叉树的深度，当二分搜索树为满二叉树，
$$2^h-1>=n$$
$$h>=log_2(n+1)$$
$$h >= O(log_2 n)$$
$$h>=O(logn)$$

当二分搜索树为斜树时，二分搜索树退化为链表，时间复杂度同链表，即 h<=n，这一问题可以使用平衡二叉树解决。
