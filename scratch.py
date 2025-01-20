# unique paths

from typing import List


class Solution:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
            Our base case(s) are as follows (this is how we know we've found the LCA):
                1. left == True and right == True: this means that the current node's children contain p and q; this 
                   will return the currentNode the first time this occurs (line 39)
                2. currentNode == p/q AND (left == True or right == True): this means that the current node is the top
                   of the branch and the other match, p or q, is in the same branch. 
        '''
        def recurse_tree(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Try left...
            left = recurse_tree(current_node.left)

            # Try right
            right = recurse_tree(current_node.right)

            # Only get here when we get to the end of the branch
            # Set found = True if it matches p or q
            found = current_node == p or current_node == q

            # If current node is p or q and we have found p or q in another downstream node
            # return the current node because it's the LCA
            if (found and left) or (found and right) or (left and right):
                self.ans = current_node

            # Otherwise return true because the current node or a downstream node is p or q
            # So this needs to bubble up the recursive call stack for evaluation
            return found or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans
        

# T: O(N/2 + N) -> O(N) - at worst, we're evaluating N/2 + N - l
# S: O(1) - constant space requirement
    
s = Solution()
print(s.validPalindrome("aba"))
print(s.validPalindrome("abca"))
print(s.validPalindrome("abc"))