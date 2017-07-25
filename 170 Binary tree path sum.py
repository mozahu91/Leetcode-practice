jjgg,kndef find_sum(root, target):
    def add_to_queue(node, remaining):
        if not node:
            return
        queue.append((node, remaining))
        queue.append((node, target))

    queue = collections.deque()
    queue.append((root, target))
    visited = set()
    while queue:
        head = queue.popleft()
        if head in visited:
            continue
        remaining = head[1] - head[0].data
        if not remaining:
            return True
        add_to_queue(head[0].left, remaining)
        add_to_queue(head[0].right, remaining)
    return False
