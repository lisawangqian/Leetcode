'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
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
    # @param {integer} sum
    # @return {boolean}
    def hasPathSum(self, root, sum):
        if not root:
            return False
        elif (not root.left) and (not root.right):
            return root.val == sum
        else:
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)
'''            
                    
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
            
        
       
        stack = [(root, sum)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == curr.val:
                return True

            if curr.left:
                stack.append((curr.left, val - curr.val))
            if curr.right:
                stack.append((curr.right, val - curr.val))

        return False    
        
            