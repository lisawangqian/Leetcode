'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        
        while root:
            if abs(closest - target) > abs(root.val - target):
                closest = root.val
            
            if target > root.val:
                root = root.right
            else:
                root = root.left
        
        return closest
        