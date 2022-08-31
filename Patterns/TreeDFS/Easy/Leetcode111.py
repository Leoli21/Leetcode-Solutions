# Recursive DFS
import collections


def minDepth(root):
    # Corner Case. Should never be hit unless we encounter a
    # node with a 'None' value.
    if root is None:
        return 0

    # Base Case : Leaf node. A leaf node has a depth of 1
    if root.left is None and root.right is None:
        return 1

    # If left subtree is None, recur for right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    # If right subtree is None , recur for left subtree
    if root.right is None:
        return minDepth(root.left) + 1

    # Otherwise, if both left and right subtree exist, recur
    # both left and right subtree and return the minimum + 1
    # to account for the root node as part of the depth.
    return min(minDepth(root.left), minDepth(root.right)) + 1

# BFS Solution
def minDepth(self, root):
    if not root:
        return 0

    # Tree has at least one node
    q = collections.deque([(root, 1)])
    while q:
        node, depth = q.popleft()
        # If we pop a null node, we end up just skipping
        # it and popping the next node in queue
        if node:
            # The first leaf node that we encounter, will be
            # our answer
            if not node.left and not node.right:
                return depth
            else:
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
