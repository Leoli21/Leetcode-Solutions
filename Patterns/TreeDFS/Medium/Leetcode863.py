# Constructs a map that maps each node to its parent.
# Then performs DFS to retrieve all nodes within the given distance
# using parent map.
import collections
from collections import defaultdict


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


# Solution that constructs a graph of the Tree using DFS and
# then performs BFS on the graph to find the nodes distance k
# from target
def distanceK(self, root, target, k):
    graph = defaultdict(list)

    self.buildGraph(root, None, graph)

    q = collections.deque([(target, 0)])

    visited = set()

    res = []
    while q:
        node, distance = q.popleft()
        if node in visited:
            continue

        visited.add(node)

        if distance == k:
            res.append(node.val)

        elif distance < k:
            for child in graph[node]:
                q.append((child, distance + 1))

    return res

def buildGraph(self, node, parent, graph):
    if not node:
        return node

    if parent:
        graph[node].append(parent)

    if node.left:
        graph[node].append(node.left)
        self.buildGraph(node.left, node, graph)

    if node.right:
        graph[node].append(node.right)
        self.buildGraph(node.right, node, graph)