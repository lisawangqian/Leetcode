
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''




class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
        elif root.left==None:
            return 1+self.minDepth(root.right)
        elif root.right==None:
            return 1+self.minDepth(root.left)
        else:
            return 1+min(self.minDepth(root.right), self.minDepth(root.left))

'''
      

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        m = 2147483647     
        stack = [(root, 1)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right:
                m = min (m, val)

            if curr.left:
                stack.append((curr.left, val + 1))
            if curr.right:
                stack.append((curr.right, val + 1))

        return m
'''