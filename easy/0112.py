# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        def helper(node, current_sum):
            if node is None:
                return False
            
            current_sum += node.val
            
            # Check if it's a leaf node and the sum equals targetSum
            if node.left is None and node.right is None:
                return current_sum == targetSum
            
            # Recursively check either subtree (using OR)
            return helper(node.left, current_sum) or helper(node.right, current_sum)
        
        return helper(root, 0)
