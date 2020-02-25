# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        dic = set()
        dic.add(head.val)
        node = head
        while node.next:
            if node.next.val in dic:
                node.next = node.next.next
            else: 
                dic.add(node.next.val)
                node = node.next
        return head