'''
Remove all elements from a linked list of integers that have value val.


'''



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head and head.val == val:
            head = head.next
        
        if not head:
            return None
        
        current = head
        
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
            
        return head