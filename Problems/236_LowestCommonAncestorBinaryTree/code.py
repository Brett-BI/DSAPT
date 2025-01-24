# Definition for a binary tree node.
from collections import deque
from typing import Any, Optional


class TreeNode:
    def __init__(self, x: Any, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = x
        self.left = left
        self.right = right
    
    # TODO: Add comparison dunder methods so that TreeNodes can be compared to 
    # other tree nodes.

    # TODO: Add function to spit out text representation of tree graph.

# for [3,5,1,6,2,0,8,null,null,7,4]
BinaryTree = TreeNode(3)
BinaryTree.left = TreeNode(5)
BinaryTree.left.left = TreeNode(6)
BinaryTree.left.right = TreeNode(2)
BinaryTree.left.right.left = TreeNode(7)
BinaryTree.left.right.right = TreeNode(4)
BinaryTree.right = TreeNode(1)
BinaryTree.right.left = TreeNode(0)
BinaryTree.right.right = TreeNode(8)

print(BinaryTree)
print(BinaryTree.left.val)
print(BinaryTree.left.left)
print(BinaryTree.left.right)

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

    def LCAIterative(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # use a queue to work through each of the nodes in the tree
        q = deque([root])

        # use a dictionary to keep track of the node and its parent node
        # key is the current node, value is its parent
        parent = {root: None}

        # while there's something in the queue, evaluate each item
        # this is only necessary to get p and q in the parent dictionary
        while q:
            # current working node; remove the left-most element (first) from the queue
            currentNode = q.popleft()

            # if it has a left and/or right child, append the child to the queue
            # then add the node and its parent to the parent dictionary
            if currentNode.left:
                q.append(currentNode.left)
                parent[currentNode.left] = currentNode

            if currentNode.right:
                q.append(currentNode.right)
                parent[currentNode.right] = currentNode
            
            # stop processing the queue when we've found p and q
            if p in parent and q in parent:
                break
        
        # use a set to keep track of ancestors; this has an O(1) lookup time
        # behind the scenes, a set is implemented as a hash table - a key with no value
        ancestors = set()

        # while p exists (p is going to change as we bubble up the parent hierarchy)
        while p:
            # add current p
            ancestors.add(p)
            # set new p to the previous p's parent node
            p = parent[p]

        # while q exists (we're going to exhaust all elements with q as the parent just like
        # we did with p), bubble up its parent and add to ancestors
        # as soon as q is in the ancestors set, return
        while q: 
            if q in ancestors:
                return q
            q = parent[q]

    def LCARecursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        '''
            Our base case(s) are as follows (this is how we know we've found the LCA):
                1. left == True and right == True: this means that the current node's children contain p and q; this 
                   will return the currentNode the first time this occurs (line 39)
                2. currentNode == p/q AND (left == True or right == True): this means that the current node is the top
                   of the branch and the other match, p or q, is in the same branch. 
        '''
        def traverse(current_node: TreeNode) -> bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Try left...
            left = traverse(current_node.left)

            # Try right
            right = traverse(current_node.right)

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
        traverse(root)
        return self.ans

# NOTE: p and q are actually the entire branches, not single tree nodes with no children.
s = Solution()
a = s.lowestCommonAncestor(BinaryTree, TreeNode(5), TreeNode(1))
print(a)

# Complexity
# Based on the size of the tree
# T: O(N) where N = number of nodes
# S: O(1) because we're not using extra space/data structures BUT the recursive 
# stack frames will place this in O(N) because 1 strack is used per function call