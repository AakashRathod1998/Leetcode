# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def compare(node, low, high):

            if not node:
                return True

            if not (low < node.val < high):
                return False

            return compare(node.left, low, node.val) and compare(node.right, node.val, high)

        return compare(root, -math.inf, math.inf)
