from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: Optional[TreeNode], right: Optional[TreeNode]) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution():
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lca(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node





"""
Short Solutions

To do:
125_valid_palindrome.py                                 
x346_moving_average_from_data_stream.py
1436_destination_city.py                                
235_lowest_common_ancestory_of_a_binary_search_tree.py  
x791_custom_sort_string.py
339_nested_list_weight_sum.py

Complete:
20_valid_parentheses.py                                 
x62_unique_paths.py
x71_simplify_path.py
x56_merge_intervals.py
215_kth_largest_element_in_an_array.py  
x938_range_sum_of_bst.py  
"""