# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Depth First Search Binary Tree

class Solution(object):

    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def dfs(leaf, path):
            if leaf.left == None and leaf.right == None:
                self.rtype.append(path)
            if leaf.left:
                dfs(leaf.left, path + "->" + str(leaf.left.val))
            if leaf.right:
                dfs(leaf.right, path + "->" + str(leaf.right.val))
            
            
        self.rtype = []
        if root == None:
            return self.rtype
        else:
            dfs(root, str(root.val))
        return self.rtype
        
            
        