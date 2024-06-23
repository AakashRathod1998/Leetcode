# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(root, subRoot):

            if (not root) or (not subRoot):
                return not root and not subRoot

            return (root.val == subRoot.val) and compare(root.left, subRoot.left) and compare(root.right, subRoot.right)

        def dfs(root):

            if not root:
                return False
            elif root.val == subRoot.val and (compare(root.left, subRoot.left) and compare(root.right, subRoot.right)):
                return True

            return dfs(root.left) or dfs(root.right)

        return dfs(root) 
