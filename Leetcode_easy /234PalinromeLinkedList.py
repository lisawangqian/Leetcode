'''
Given a singly linked list, determine if it is a palindrome.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
            
        fast, slow = head, head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
        phalf, last = slow.next, None
        while phalf:
            next = phalf.next
            phalf.next = last
            last, phalf = phalf, next
            
        p1, p2 = head, last
        while p2 and p1.val == p2.val:
            p1 = p1.next
            p2 = p2.next
        
        if not p2:
            return True
        else:
            return False
            
        