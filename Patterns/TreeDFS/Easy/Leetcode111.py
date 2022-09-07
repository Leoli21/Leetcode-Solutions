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

    # If left subtree is None, we just use the depth of the
    # right subtree
    if root.left is None:
        return minDepth(root.right) + 1

    # If right subtree is None, we just use the depth of the
    # left subtree
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
    q = collections.deque([root])

    # Maintain a variable that indicates the current depth
    # of the tree we are exploring
    depth = 1
    while q:
        for i in range(len(q)):
            node = q.popleft()

            # If leaf node (no left or right children, return the depth)
            # Essentially we are looking for the first leaf node that we encounter
            # and returning the depth where that first leaf node is found.
            if not node.left and not node.right:
                return depth
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # Increase depth by one after finishing traversing a level
        depth += 1

