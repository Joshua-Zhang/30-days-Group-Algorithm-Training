# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.INF,self.ans=-0x7ffffff,-0x7ffffff       
        self.dfs(root)
        return self.ans
        
    def dfs(self,root):
        if not root:
            return self.INF
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.ans = max(self.ans, max(left, right) + root.val, left + right + root.val, root.val)
        return max(root.val, root.val + max(left, right))