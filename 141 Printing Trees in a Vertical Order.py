"""
We need to check the Horizontal Distances from root for all nodes. If two nodes have the same Horizontal Distance (HD), then they are on same vertical line. The idea of HD is simple. HD for root is 0, a right edge (edge connecting to right subtree) is considered as +1 horizontal distance and a left edge is considered as -1 horizontal distance. For example, in the above tree, HD for Node 4 is at -2, HD for Node 2 is -1, HD for 5 and 6 is 0 and HD for node 7 is +2.
This is the easiest way to solve it. O(n) is the complexity. Very important question

"""

def VerticalOrder(root):
    nodes = collections.defaultdict(list)
    queue = collections.deque([(root,0)])
    while queue:
        node,pos = queue.popleft()
        if not node:
            continue
        nodes[pos].append(node)
        queue.append((node.left,pos-1))
        queue.append((node.right, pos+1))
    return [nodes[i] for i in sorted(nodes)]
