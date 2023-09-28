# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return Solution.isMirror(root.left, root.right)

    def isMirror(left: TreeNode, right: TreeNode) -> bool:
        # Base cases
        if not left and not right:
            return True
        if not left or not right:
            return False

        # Check current nodes and recurse for children
        return (left.val == right.val) and Solution.isMirror(left.left, right.right) and Solution.isMirror(left.right, right.left)
