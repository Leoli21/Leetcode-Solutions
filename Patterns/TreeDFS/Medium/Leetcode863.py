
import collections
from collections import defaultdict

# Solution that constructs a graph of the Tree using DFS and
# then performs BFS on the graph to find the nodes distance k
# from target
def distanceK(self, root, target, k):
    # The graph dictionary will essentially map every node with its neighboring
    # nodes. This includes it's parent, left, and right.
    # For example:
    # graph = {
    #   3: [5, 1],
    #   5: [3, 6, 2],
    #   6: [5],
    #   etc...
    # }
    graph = collections.defaultdict(list)

    # Construct our graph using DFS
    self.buildGraph(root, None, graph)

    # Conduct a BFS on the graph to find all nodes distance 'k' from
    # the target

    # Each entry in our deque will be a tuple, (node, distance), representing
    # the current node and it's distance from the target
    q = collections.deque([(target, 0)])
    res = []
    visited = set()

    while q:
        # Get the current node from queue and it's distance
        node, dist = q.popleft()

        # If we have already visited this current node, then just continue
        # with next element in our queue
        if node in visited:
            continue

        # Add it to our visited nodes, so that we do not enounter it again
        # in our BFS and risk adding it to our 'res' twice
        visited.add(node)

        # Check if we have reached nodes that are distance 'k' from
        # target
        if dist == k:
            res.append(node.val)

        # Check if we still need to traverse more levels of the graph
        elif dist < k:
            # Add the current node's neighbors using the 'graph' dictionary
            # to our queue for exploration in our next iteration
            for child in graph[node]:
                q.append((child, dist + 1))

    return res


def buildGraph(self, node, parent, graph):
    # If reach a 'None' node, just do nothing and return
    if not node:
        return None

    # If our node has a parent, add it as a neighbor to it's entry
    # in the graph
    if parent:
        graph[node].append(parent)

    # If our node has a left child, add it as an entry to the graph
    # Then explore it's left child
    if node.left:
        graph[node].append(node.left)
        self.buildGraph(node.left, node, graph)

    # If our node has a right child, add it as an entry to the graph
    # Then explore it's right child.
    if node.right:
        graph[node].append(node.right)
        self.buildGraph(node.right, node, graph)