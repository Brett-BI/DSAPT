# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Return None if root doesn't exist because there is nothing to search (only 
        # useful if there is no guarantee that a node will exist)
        if not root:
            return None # return this to end the recursive function call here
        
        # Return the parent Node if a match is found (meaning the Node matches p or q)
        if root == p or root == q:
            return root # return this to end the recursive function call here
        
        # Note that the case that is not covered above is the one where root != p|q.
        # This forces another recursive function call to happen because the code 
        # execution continues to the function calls below

        # recursively iterate
        # this is going to iterate over each node until root is None or a match is found
        # for both the left and the right (based on match logic above)
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        # if both the left and right children aren't null/None, the parent is the ancestor
        if l and r:
            return root

        # if left or right child is null, the match is on the same branch so we can 
        # return the match we have (because a node can be a descendant of itself)
        return l or r


# Complexity
# Based on the size of the tree
# T: O(N) where N = number of nodes
# S: O(1) because we're not using extra space/data structures BUT the recursive 
# stack frames will place this in O(N) because 1 strack is used per function call