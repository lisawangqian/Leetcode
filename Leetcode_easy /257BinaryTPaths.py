'''
Given a binary tree, return all root-to-leaf paths.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        stack = [(root, str(root.val))]
        result = []
        while stack:
            curr, s = stack.pop()
            if not curr.left and not curr.right:
                result.append(s)

            if curr.left:
                stack.append((curr.left, s + "->" + str(curr.left.val)))
            if curr.right:
                stack.append((curr.right, s + "->" + str(curr.right.val)))
                
        return result