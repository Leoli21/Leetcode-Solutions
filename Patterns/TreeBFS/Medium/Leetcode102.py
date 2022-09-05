import collections

def levelOrder(self, root):
    if not root: return []
    q = collections.deque([root])
    res = []
    while q:
        currLevel = []
        numNodes = len(q)
        for i in range(numNodes):
            node = q.popleft()
            currLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(currLevel)
    return res