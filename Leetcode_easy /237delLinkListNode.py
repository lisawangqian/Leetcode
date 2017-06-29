'''
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node and node.next:
                node.val = node.next.val
                tem = node.next.next
                del node.next
                node.next = tem