'''
Given a linked list, swap every two adjacent nodes and return its head.


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (not head) or (not head.next):
            return head
        
        new = ListNode(0)
        new.next = head
        current = new
        while current.next and current.next.next:
            tem1 = current.next
            tem2 = current.next.next
            current.next = tem2
            tem1.next = tem2.next
            tem2.next = tem1
            current = current.next.next
            
            
        return new.next
        