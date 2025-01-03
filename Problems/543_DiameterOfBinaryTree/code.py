from typing import Any, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = x
        self.left = left
        self.right = right

root = TreeNode(1)
# [1]
root.left = TreeNode(2)
root.right = TreeNode(3)
# [(1), (2, 3)]
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left =  TreeNode(6)
root.right.right = TreeNode(7)
# [(1), (2, 3), (4, 5, 6, 7)]
root.right.left.right = TreeNode(8)
root.right.left.left = TreeNode(9)
# [(1), (2, 3), (4, 5, 6, 7), (None, None, None, None, 8, 9, None, None)]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0 # diameter is the sum of the length of longest branches

        def longest_path(node: TreeNode):
            if not node:
                return 0
            
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)
            # set max discovered diameter
            diameter = max(diameter, left_path + right_path)        
            # return current node/branch depth
            return max(left_path, right_path) + 1
        
        longest_path(root)

        return diameter

s = Solution()
a = s.diameterOfBinaryTree(root)
print(a)


# T: O(n)
# One function call per node in the binary tree. The max() function
# operates in constant time O(1) and constants are ignored.
# S: O(2n + 1) -> O(n)
# Ignore constants 