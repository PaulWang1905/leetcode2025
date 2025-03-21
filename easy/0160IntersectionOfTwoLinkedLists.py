# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # If either list is empty, there can't be an intersection
        if not headA or not headB:
            return None
            
        # Two-pointer approach
        pointerA = headA
        pointerB = headB
        
        # If the lists have different lengths, this approach will eventually
        # synchronize the pointers to start at the same distance from the intersection
        while pointerA != pointerB:
            # When pointer reaches the end of list A, redirect to head of list B
            pointerA = headB if pointerA is None else pointerA.next
            
            # When pointer reaches the end of list B, redirect to head of list A
            pointerB = headA if pointerB is None else pointerB.next
            
            # If there's no intersection, both pointers will eventually become None
            # If there is an intersection, they'll meet at the intersection node
        
        # Return either pointer (they're either both None or both at intersection)
        return pointerA
