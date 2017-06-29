'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},

'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
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
        
        return new[::-1]