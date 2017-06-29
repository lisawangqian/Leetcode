'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        level = [root]
        lst = [root]
        new = [[root.val]]
        while level:
            level = []
            subLevel = []
            for node in lst:
                if node.left:
                    level.append(node.left)
                    subLevel.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    subLevel.append(node.right.val)
            if level:
               new.append(subLevel)
            lst = level[:]
        
        return new











      '''def levelOrder(self, root):
        result=[]
        if root==None:
            return result
        k=0
        result.append([root.val])
        level=[root.left, root.right]
        lst=[root.left, root.right]
        while lst:
            k+=1
            result.append([])
            for node in level:
                if node != None:
                    result[k].append(node.val)
            lst=[]
            for node in level:
                if node != None:
                    lst.append (node.left)
                    lst.append (node.right)
            level=lst[:]
        del result[-1]
        return result 
        '''