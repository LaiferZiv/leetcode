#Definition for singly-linked list.
from os.path import curdir


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def reorderList(self, head) -> None:
        #edge case
        if not head or not head.next or not head.next.next:
            return

        #split list to 2
        slow , fast = head , head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        #reverse second list
        prev , cur = None , second

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        #unite
        first = head
        second = prev
        while second:
            tmp1 , tmp2 = first.next , second.next
            first.next = second
            second.next = tmp1
            first , second = tmp1 , tmp2



