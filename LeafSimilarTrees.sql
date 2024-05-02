# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_tree_sum(root):
            stack = [root]
            li = []

            while stack:

                node = stack.pop()

                if not node.left and not node.right:
                    li.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return li

        return get_tree_sum(root1) == get_tree_sum(root2)
