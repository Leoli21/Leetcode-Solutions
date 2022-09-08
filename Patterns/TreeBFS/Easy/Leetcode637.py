import collections

# BFS: Level Order Traversal
def averageOfLevels(self, root):
    q = collections.deque([root])
    res = []
    while q:
        levelSum = 0
        numNodes = len(q)
        for i in range(numNodes):
            node = q.popleft()
            levelSum += node.val
            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
        res.append(levelSum / numNodes)
    return res

# DFS Solution
def averageOfLevels(self, root):
    info = []

    def depth(node, dep):
        if not node:
            return None
        # This checks if there is already an entry in 'info' for the
        # current depth. If not, then we add an entry to 'info' for the
        # current depth.
        if len(info) < dep:
            info.append([0, 0])

        # We have to use dep - 1 because our depth starts at 1 while arrays
        # are 0-indexed.
        info[dep - 1][0] += 1
        info[dep - 1][1] += node.val
        depth(node.left, dep + 1)
        depth(node.right, dep + 1)

    depth(root, 1)
    res = []
    for count, summ in info:
        res.append(summ / count)
    return res
