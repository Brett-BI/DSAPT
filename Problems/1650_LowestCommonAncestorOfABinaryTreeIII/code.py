

from typing import Optional


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestorIterative(self, p: Node, q: Node) -> Optional[Node]:
        """
        Returns the lowest common ancestor node that is shared with p and q
        in a binary tree. The Node object has a parent attribute. This is an 
        iterative approach. NOTE: this is nearly identical to the LCA iterative 
        solution.

        Time complexity: O(H) where H = height of the tree
        Space complexity: O(H) where H = height of the tree

        Parameters:
        p (Node): a Node object with an ancestor in the binary tree
        q (Node): a Node object with an ancestor in the binary tree

        Returns:
        Node: the lowest common ancestor node of p and q
        """
        path: set[Node] = set()

        while p:
            path.add(p)
            p = p.parent
        
        while q:
            if q in path:
                return q
            q = q.parent

        return None



    def lowestCommonAncestorRecursive(self, p: Node, q: Node) -> Optional[Node]:
        """
        Returns the lowest common ancestor node that is shared with p and q 
        in a binary tree. The Node object has a parent attribute.

        Time complexity: O(H) where H = height of the tree
        Space complexity: O(H) where H = height of the tree

        Parameters:
        p (Node): a Node object with an ancestor in the binary tree
        q (Node): a Node object with an ancestor in the binary tree

        Returns:
        Node: the lowest common ancestor node of p and q
        """
        # track the nodes we've found - they're all unique
        discoveredNodes: set = set()

        def dfs(node: Optional[Node]) -> Optional[Node]:
            nonlocal discoveredNodes

            # we've found the root of the tree or the first shared Node
            if not node or node in discoveredNodes:
                return node
            
            discoveredNodes.add(node)
            return dfs(node.parent)
        
        # one node may be at a different depth so try both
        return dfs(p) or dfs(q)
    
