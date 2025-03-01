'''
101. Symmetric Tree
Solved
Easy
Topics
Companies

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 

Constraints:

    The number of nodes in the tree is in the range [1, 1000].
    -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Handle empty tree case.
        if not root:
            return True

        def helper(leftNode, rightNode):
            if leftNode is None and rightNode is None:
                return True
            if not leftNode or not rightNode:
                return False
            if leftNode.val != rightNode.val:
                return False
            # Compare the left subtree of the left node with the right subtree of the right node,
            # and the right subtree of the left node with the left subtree of the right node.
            return helper(leftNode.left, rightNode.right) and helper(leftNode.right, rightNode.left)
        
        return helper(root.left, root.right)
