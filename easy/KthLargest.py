# Definition for singly-linked list.
from heapq import heapify, heappush, heappop
from typing import Optional, List


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #edge cases
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            head = primary = list1
            secondary = list2
        else:
            head = primary = list2
            secondary = list1
        while primary and secondary:
            if primary.val <= secondary.val :
                prev = primary
                primary = primary.next
            else:
                prev.next = secondary
                tmp = primary
                primary = secondary
                secondary = tmp
        return head

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mapchar_s = {}
        mapchar_t = {}
        for char_s,char_t in (s,t):
            mapchar_s[char_s] = mapchar_s.get(char_s,0) + 1
            mapchar_t[char_t] = mapchar_t.get(char_t,0) + 1
        return mapchar_t == mapchar_s

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            t1 = s[left]
            t2 = s[right]
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapify(self.heap)

    def add(self, val: int) -> int:
        ans = 0
        heappush(self.heap,val)
        for i in range(self.k):
            ans = heappop(self.heap)
        return ans
if __name__ == "__main__":
    print('hello world')


