# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        
        newhead=head.next
        current=head
        previous=None
        while current!=None and current.next!=None:
            if previous!=None:
                previous.next=current.next
            previous=current
            
            tem1=current
            tem2=current.next.next
            current=current.next
            current.next=tem1
            current.next.next=tem2
            
            current=current.next.next
        
        return newhead
            
            