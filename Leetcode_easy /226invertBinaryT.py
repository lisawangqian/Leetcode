'''
Invert a binary tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        lst = [root]
        level = [root]
        while level:
            level = []
            for node in lst:
                if node.left and node.right:
                    tem = node.left
                    node.left = node.right
                    node.right = tem
                    level.append(node.left)
                    level.append(node.right)
                elif node.left:
                    node.right = node.left
                    node.left = None
                    level.append(node.right)
                elif node.right:
                    node.left = node.right
                    node.right = None
                    level.append(node.left)
                    
            lst = level[:]
        
        return root
       