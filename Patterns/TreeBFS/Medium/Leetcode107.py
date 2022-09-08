import collections

# DFS w/ Recursion
def levelOrderBottom(self, root):
    res = []
    self.dfs(root, 0, res)
    return res


def dfs(self, node, level, res):
    if node:
        # Since level starts at 0, the length of an array will always be
        # 1 greater than the level value. (For a node with a depth of 2,
        # this node should be added to the array at index -3 of resulting
        # array.

        # Example to make this condition more clear:
        # self.dfs(3, 0, res)
        # len(res) is current 0 which is less than 0 + 1.
        # Thus we need to create an array to represent the first level.
        # We create an empty array an insert it at the beginning of the result
        # array.
        if len(res) < level + 1:
            res.insert(0, [])

        # -(level + 1) will give us the correct position of the array that we
        # need to append our current node's value to. It is at the end because
        # the resulting array is in reverse order (bottom up)
        res[-(level + 1)].append(node.val)
        self.dfs(node.left, level + 1, res)
        self.dfs(node.right, level + 1, res)

# DFS w/ Stack
def levelOrderBottom(self, root):
    if not root:
        return []

    res = []
    stack = [(root, 1)]
    while stack:
        node, depth = stack.pop()
        if len(res) < depth:
            res.insert(0, [])

        # Make sure to use the index of '-depth' because we are constantly
        # inserting new arrays to the front of res and thus the index ordering
        # of our array is reversed.
        # nodes at depth 1 are at -1 in res (or the last array in res)
        # nodes at depth 2 are at -2 in res (or the second to last array in res)
        # nodes at depth 3 are at -3 in res
        res[-depth].append(node.val)

        # Append the right child first because then we end
        # up evaluating the left child first when popping from
        # the stack. This ensures the correct order of processing.
        # Left Child -> Right Child
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    return res

# BFS
def levelOrderBottom(self, root):
    if not root:
        return []
    res = collections.deque()
    q = collections.deque([root])
    while q:
        numNodes = len(q)
        currLevel = []
        for i in range(numNodes):
            node = q.popleft()
            currLevel.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        res.appendleft(currLevel)
    return res