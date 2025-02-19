from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes_amount = 0
        prev = None
        cur = head

        while cur:
            nodes_amount += 1
            cur = cur.next
        location = nodes_amount - n
        if location < 0 :
            return head
        elif location == 0 :
            tmp = head.next
            head.next = None
            return tmp
        cur = head
        for _ in range(location):
            prev = cur
            cur = cur.next

        prev.next = cur.next
        cur.next = None
        return head
