from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        vertical_order = defaultdict(list)
        
        queue = deque([(root, 0)])
        
        while queue:

            node, col = queue.popleft()
            vertical_order[col].append(node.val) 
            # print(vertical_order, col) 

            if node.left:
                queue.append((node.left, col + 1))

            if node.right:
                queue.append((node.right, col + 1))
                

        all_keys = sorted(vertical_order.keys())
        print(all_keys) 

        return [vertical_order[i] for i in all_keys]
