# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        out=ListNode(0)
        a=out
        flag=0
        while l1!=None and l2!=None:
            d=l1.val+l2.val+flag
            a.next=ListNode(d%10)
            flag=d//10
            l1=l1.next
            l2=l2.next
            a=a.next
        if l1!=None:
            while l1!=None:
                d=l1.val+flag
                a.next=ListNode(d%10)
                flag=d//10
                l1=l1.next
                a=a.next
        if l2!=None:
            while l2!=None:
                d=l2.val+flag
                a.next=ListNode(d%10)
                flag=d//10
                l2=l2.next
                a=a.next
        if flag!=0:
            a.next=ListNode(flag)
        return out.next
            