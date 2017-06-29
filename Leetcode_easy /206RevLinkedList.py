
'''
Reverse a singly linked list.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        
        current = None
        while head:
            vnext = head.next
            head.next = current
            current = head
            head = vnext
        
        return current
            