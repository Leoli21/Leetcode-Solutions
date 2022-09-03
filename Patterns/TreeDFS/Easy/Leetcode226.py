import collections

# BFS with Queue
def invertTree(self, root):
    queue = collections.deque([root])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

# Iterative DFS using Stack
def invertTree(self, root):
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.extend([node.right, node.left])
    return root


# Recursive DFS
def invertTree(self, root):
    # If current root is empty:
    # There are no children to swap, so just return
    # the current 'root'
    if not root:
        return root

    # We must store the left subtree of root into a 'temp' variable because
    # when we call root.left = self.invertTree(root.right), 'root.left' ends up
    # becoming the value of root.right.
    # So if you don't store the left subtree in a 'temp', you end up passing
    # root.right to root left and root.right to root.right as well b/c root.left
    # was changed to root.right before.
    '''
    temp = root.left
    root.left = self.invertTree(root.right)
    root.right = self.invertTree(temp)
    return root
    
    '''

    # Swap the left and right children while calling invertTree() on the root's
    # children so that by the time the swap occurs, the children of the 'root'
    # are already all swapped.
    root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

    return root


