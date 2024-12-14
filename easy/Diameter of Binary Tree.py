from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal max_edges
            if not node:
                return -1

            l_edges = helper(node.left) + 1
            r_edges = helper(node.right) + 1

            max_edges = max(max_edges, l_edges + r_edges)
            return max(l_edges, r_edges)

        max_edges = 0
        helper(root)
        return max_edges
