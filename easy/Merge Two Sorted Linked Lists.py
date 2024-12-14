from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        #where to start
        (primary,secondary) = (list1,list2) if list1.val < list2.val else (list2,list1)
        head = prev = primary
        primary = primary.next
        #compare each node between the lists
        while primary and secondary:
            cur = primary if primary.val < secondary.val else secondary
            prev.next = cur
            prev = prev.next
            if cur is primary:
                primary = primary.next
            else:
                secondary = secondary.next

        prev.next = secondary if not primary else primary
        return head


