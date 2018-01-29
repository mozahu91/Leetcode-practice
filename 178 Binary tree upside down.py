"""
Binary Tree Upside Down
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the
 same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left 
 leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
  """
  
  class Solution:
        # @param root, a tree node
        # @return root of the upside down tree
        def upsideDownBinaryTree(self, root):
            # take care of the empty case
            if not root:
                return root
            # take care of the root
            l = root.left
            r = root.right
            root.left = None
            root.right = None
            # update the left and the right children, form the new tree, update root
            while l:
                newL = l.left
                newR = l.right
                l.left = r
                l.right = root
                root = l
                l = newL
                r = newR
            return root
