# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr_plus = head
        while curr_plus and curr_plus.next:
            curr = curr.next
            curr_plus = curr_plus.next.next
            if curr_plus == curr:
                return True
        return False