"""
Depending on the complexity of the question, if they ask to Shortest paths first Then go to BFS else DFS.
Here, I will show both the approaches:
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
c = TreeNode(1)
c.left = TreeNode(2)
c.right = TreeNode(3)
c.left.right = TreeNode(5)


def binaryTreePaths2(root):
    if not root:
        return []
    res, queue = [], collections.deque([(root, "")])
    while queue:
        node, ls = queue.popleft()

        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.left:
            queue.append((node.left, ls+str(node.val)+"->"))
            #print(list(queue))
        if node.right:
            queue.append((node.right, ls+str(node.val)+"->"))
    return res
    
    def binaryTreepaths(root):
    if not root:
        return []
    
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
        
    return res
