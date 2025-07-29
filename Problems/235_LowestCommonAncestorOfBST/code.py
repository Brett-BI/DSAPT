# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestorIter(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Returns the lowest common ancestor of two TreeNode objects, p and q in a binary search tree 
            by iteration.

            Parameters:
            root (TreeNode): The root TreeNode of the Binary Search Tree
            p (TreeNode): a TreeNode in the binary search tree
            q (TreeNode): a TreeNode in the binary search tree

            Returns:
            TreeNode: the lowest common ancestor of p and q in the binary search tree
        """
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node

        return root
            
    def lowestCommonAncestorRecursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
            Returns the lowest common ancestor of two TreeNode objects, p and q in a binary search tree
            by recursion.

            Parameters:
            root (TreeNode): The root TreeNode of the Binary Search Tree
            p (TreeNode): a TreeNode in the binary search tree
            q (TreeNode): a TreeNode in the binary search tree

            Returns:
            TreeNode: the lowest common ancestor of p and q in the binary search tree
        """
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestorRecursive(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestorRecursive(root.right, p, q)
        else:
            return root
        
s = Solution()
print(s.lowestCommonAncestorRecursive.__doc__)