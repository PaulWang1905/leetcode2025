class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            left_height = helper(node.left)
            if left_height == -1:
                return -1
            right_height = helper(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return helper(root) != -1
