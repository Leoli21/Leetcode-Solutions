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
    res = []
    info = []
    def dfs(node, depth = 0):
        if node:
            # This checks if there is already an entry in 'info' for the
            # current depth. If not, then we add an entry to 'info' for the
            # current depth.
            if len(info) <= depth:
                # If the current depth is equal to the length of 'info', that means we
                # are at the first node in the given 'depth'. This is because len(info) will
                # always be 1 greater than the depth of a given node, since depth starts at 0.
                info.append([0,0])
            info[depth][0] += node.val
            info[depth][1] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

    dfs(root)
    for summ, count in info:
        res.append(summ/count)
    return res
