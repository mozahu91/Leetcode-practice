"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root == None:
            return res
        self.dfs(root, 0, [root.val], res, sum)
        return res
    
    def dfs(self, root, currsum, valist, res, sum):
        if root.left == None and root.right == None:
            if currsum == sum-root.val:
                res.append(valist)
            return res
        if root.left:
            self.dfs(root.left, currsum+root.val, valist+[root.left.val], res, sum)
        if root.right:
            self.dfs(root.right, currsum+root.val, valist+[root.right.val], res, sum)
