'''
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

Binary search tree: left: smaller than pre; right: bigger than pre
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
       
        
        while (p.val-root.val) * (q.val-root.val) > 0: 
            if p.val > root.val:
                root = root.right
            else:
                root = root.left
    
        return root