class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def size(node):
            nonlocal ans
            if not node:
                return 0
            left = size(node.left)
            right = size(node.right)
            ans = ans and abs(left-right) <= 1
            return max(left,right) + 1
        ans = True
        size(root)
        return ans