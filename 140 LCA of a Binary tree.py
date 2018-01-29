"""
Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as
the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).
The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root.
Computation of lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1, plus the distance from the root to n2, minus twice the distance from the root to their lowest common ancestor. (Source Wiki)
                    1

               2         3

           4       5   6     7
LCA(4,5) = 2
LCA(4,6) =1
LCA(2,4) = 2
LCA(3,4) =1

"""

def lowestCommonAncestor(self, root, p, q):
    if root in None:
        return root
    
    if root == p or root ==q:
        return root
    
    left =lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)
    
    if left is not None and right is not None:
        return root
    
    if left is not None:
        return left
    
    if right is not None:
        return right
