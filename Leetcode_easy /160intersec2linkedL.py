'''
Write a program to find the node at which the intersection of two singly linked lists begins.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (not headA) or (not headB):
            return None
        
        currentA, currentB = headA, headB    
        lenA = self.getLength(headA)
        lenB = self.getLength(headB)
        
        if lenA > lenB:
            for i in range(lenA - lenB):
                currentA = currentA.next
        if lenB > lenA:
            for i in range(lenB - lenA):
                currentB = currentB.next
        while currentB and (currentB.val != currentA.val):
            currentB = currentB.next
            currentA = currentA.next
    
        return currentB
        
        
    def getLength(self, head):
        i = 0
        while head:
            i+=1
            head = head.next
        return i
            