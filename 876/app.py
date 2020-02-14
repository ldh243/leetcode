# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        len = 0
        cur = 1
        ans = head
        while head:
            len += 1
            if cur < (len // 2 + 1):
                cur += 1
                ans = ans.next
            head = head.next
        return ans