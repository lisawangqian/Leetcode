'''
Given a linked list, remove the nth node from the end of list and return its head.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head
        point = head
        
        for i in range(n):
            current = current.next
        if not current:
            head = head.next
        else:
            while current.next:
               current = current.next
               point = point.next
            tem = point.next.next
            del point.next
            point.next = tem
        
        return head
        