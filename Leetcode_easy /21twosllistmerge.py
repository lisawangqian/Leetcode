'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not(l1):
            return l2
        if not(l2):
            return l1
            
        new = ListNode(0)
        head = new
        while l1 or l2:
            if l1 and l2 and l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            elif l1 and l2:
                new.next = l2
                l2 = l2.next
            elif l1:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next
            
        return head.next