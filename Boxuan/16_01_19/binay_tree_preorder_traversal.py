# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans = []
        self.helper(ans, root)
        return ans
        
    def helper(self, ans, root):
        ans.append(root.val)
        if root.left:
            self.helper(ans, root.left)
        if root.right:
            self.helper(ans, root.right)