'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
        if root==None:
            return True
        else:
            return self.subisSymetric(root.left, root.right)
    
    def subisSymetric(self, l, r):
        if l==None and r==None:
            return True
        elif l==None or r==None:
            return False
        elif l.val==r.val:
            return self.subisSymetric(l.left, r.right) and self.subisSymetric(l.right, r.left)
        else:
            return False
            
'''
#BFS
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        level = [root]
        lst = [root]
        
        while level:
            level = []
            subLevel = []
            for node in lst:
                if node.left:
                    level.append(node.left)
                    subLevel.append(node.left.val)
                else:
                    subLevel.append("#")
                if node.right:
                    level.append(node.right)
                    subLevel.append(node.right.val)
                else:
                    subLevel.append("#")
            if level:
                while subLevel:
                    if subLevel[0] != subLevel[-1]:
                        return False
                    else:
                        subLevel.pop(0)
                        subLevel.pop(-1)
               
            lst = level[:]
            
        return True
            
            
         
        