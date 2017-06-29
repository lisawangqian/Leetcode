'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        elif abs(self.depth(root.right) - self.depth(root.left)) <= 1:
            return self.isBalanced(root.right) and self.isBalanced(root.left)
        else:
            return False
    
    
    def depth(self, root):
        if not root:
            return 0
        else:
            return 1 + max(self.depth(root.right), self.depth(root.left))
            
            