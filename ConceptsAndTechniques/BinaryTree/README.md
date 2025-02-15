# Binary Tree
Binary tree is a data structure comprised of one or many nodes. Each node has, at most, 2 child nodes (left and right). Both of these nodes are optional. 



## Definitions and Structure
**Node**: the fundamental building block of a binary tree; the tree is made up of one or more nodes

**Root**: the top-most node in the tree

**Height**: the number of edges along the longest path from root to leaf node (the last node will always be a leaf node)

**Level**: the level of a node is the number of edges between it and the root node

**Leaf**: a node without children

## Structure
Each node contains the following attributes:
- Data/value
- Left child (`None` or `Node` type)
- Right child (`None` or `Node` type)

In Python, it might be represented like this:
```python
from typing import Optional

class Node:
    def __init__(self, value: T, left: Optional["Node"] = None, right: Optional["Node"] = None):
        self.value: T = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
```

## Types
Full Binary Tree:
- Every node has either 0 or 2 children.

Complete Binary Tree:
- All levels are fully filled except possibly the last, which is filled from left to right.

Perfect Binary Tree:
- All internal nodes have exactly 2 children, and all leaf nodes are at the same level.

Balanced Binary Tree:
- For every node, the difference in height between its left and right subtrees is at most 1.

Binary Search Tree (BST):
- A special type of binary tree where the val of each node is greater than all of the values in the left subtree and less than the values in the right subtree:
    - The left child contains only values less than the node.
    - The right child contains only values greater than the node.

Degenerate (or Skewed) Binary Tree:
- A tree where each node has only one child, making it look like a linked list.

## Approaches, Patterns, and Techniques
### Depth-First Search
DFS is an approach that searches the entire lineage of a branch/path before backtracking. It is a recursive approach.

Generally has a space complexity of O(h) where `h` is the height of the tree. Time complexity is O(V) where V is the number of nodes.

Best use cases:
- Searching all paths
- Wide graphs (less memory usage)

### Breadth-First Search
BFS explores all neighboring nodes on a level before changing depths. For example:
```

    1
   / \
  2   3
 / \   \
4   5   6
```

BFS will explore in this order: 1 > 2 > 3 > 4 > 5 > 6. DFS will search in this order: 1 > 2 > 4 > 5 > 3 > 6.

Best use cases:
- Shortest path
- Exploring nodes at a particular level (or where exploring one level at a time is useful)
- Memory doesn't matter (a queue is used)

### BST
This approach is different because the tree is sorted, in a way. As noted above, the child nodes follow a pattern:
- the left child node is less than the value of the parent
- the right child node is greater than the value of the parent

This matters because the approach can make use of the relationship between the parent and child nodes.

## Problems
Medium

[#235 - Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

[#236 - Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)
