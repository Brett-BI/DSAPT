from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBSTIterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # this is using a stack, essentially
        s: List[TreeNode] = []
        ans: int = 0

        if root:
            s.append(root)

        while s:
            currentNode = s.pop()
            if currentNode.val >= low and currentNode.val <= high:
                ans += currentNode.val
            
            if currentNode.left:
                s.append(currentNode.left)

            if currentNode.right:
                s.append(currentNode.right)

        return ans

    def rangeSumBSTRecursive(self, root: Optional[TreeNode], low: int, high: int) -> int:
        vSum: int = 0

        def traverse(node: TreeNode):
            # could probably add another parameter to track this
            nonlocal vSum

            # Base case.
            # if the node we're passing in doesn't exist (e.g. the node.left == None 
            # or node.right == None, return because there's nothing to evaluate)
            if not node:
                return
            
            # We know there's a node, now check if it's val is in range
            # then append if it is in the range
            if node.val >= low and node.val <= high:
                vSum += node.val

            # recurse
            traverse(node.left)
            traverse(node.right)

        # Pre-order traversal because we're starting by evaluating the root node first        
        traverse(root)

        return vSum



        