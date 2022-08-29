import collections

# Recursive DFS
def maxDepth(self, root):
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# BFS using Deque
def maxDepth(root):
    if not root:
        return 0
        # The queue will store a tuple with node and it's current
        # level/depth
    queue = collections.deque([(root, 1)])
    while queue:
        curr, val = queue.popleft()
        # If the current node has no children, no new node's will
        # be added to the deque, and we will move on to checking
        # the rest of the current level's nodes and if they have
        # children
        if curr.left:
            queue.append((curr.left, val + 1))

        if curr.right:
            queue.append((curr.right, val + 1))

    return val

# Level by Level
def maxDepth(root):
    deque = collections.deque()
    depth = 0
    # If the root exists, we start our DFS from the root by adding
    # it to the queue
    if root:
        deque.append(root)

    while deque:
        # Get how many nodes are in current level
        size = len(deque)
        for i in range(size):
            # Get a node from level
            node = deque.popleft()
            # Check if node has a left child
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        # After adding the current level node's children, increase depth by 1 and
        # begin exploring next level
        depth += 1

        # At this point, 'deque' stores all the children of the previous level's nodes

    return depth

# DFS with Stack
def maxDepth(root):
    stack = [(root, 1)]
    depth = 0
    while stack:
        node, level = stack.pop()
        if node:
            depth = max(depth, level)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
    return depth