# Heap
Heaps are an implementation of a tree structure with a *heap property*. The heap property makes the tree ordered.

**Heap Property**: ensures a specific order of elements based on a comparison. This ensures that each node is ordered using this comparison.

## Common Heaps
## Binary Tree Heap
Uses a binary tree structure and is a complete tree which means that all levels, except the last, are filled and the last level is filled from left to right without gaps.

Min-heap
A type of binary tree heap. The value of the parent node in a min-heap is always less than or equal to the values of its children. The smallest value in the tree is the root.

Max-heap
A type of binary tree heap. The value of a parent node in a max-heap is always greater than or equal to the values of its children. The largest value in the tree is that root.

Big-O
Insertion: O(logN); insertion is at the next available element to satisfy completeness then the heap property is run over the tree to sort/ensure the proper order.
Deletion: O(logN)
Retrieve max/min value: O(1)