# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(p,q):
            if p == None and q == None:
                return True
            if p == None and q:
                return False
            if p and q == None:
                return False
            if q and p:
                if p.val == q.val:
                    if isSame(p.left, q.left):
                        if isSame(p.right,q.right):
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        return isSame(p, q)