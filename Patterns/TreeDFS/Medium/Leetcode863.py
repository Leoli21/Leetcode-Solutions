def buildParentMap(self, node, parent, parentMap):
    if node is None:
        return

    parentMap[node] = parent
    self.buildParentMap(node.left, node, parentMap)
    self.buildParentMap(node.right, node, parentMap)

def distanceK(self, root, target, k):
    # Dictionary storing a node mapped to its parent node
    parentMap = {}

    # Use DFS to build a map that maps a node to its parent
    self.buildParentMap(root, None, parentMap)

    # Keep track of which nodes have been visited
    visited = set()
    res = []

    # DFS used to retrieve the nodes within the given distance
    # Start from the target node
    def dfs(node, distance):
        if node is None or node in visited:
            return

        visited.add(node)

        if distance == k:
            res.append(node.val)

        elif distance < k:
            dfs(node.left, distance + 1)
            dfs(node.right, distance + 1)
            dfs(parentMap[node], distance + 1)
    dfs(target, 0)
    return res