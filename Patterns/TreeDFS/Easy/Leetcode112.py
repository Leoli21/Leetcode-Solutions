def hasPathSum(root, targetSum):
    # We have reached the bottom of a path and have
    # not found a sum = 'targetSum'
    if not root:
        return False

    # We have reached a leaf node and the current node's value is
    # the remaining value we need to reach our targetSum
    if not root.left and not root.right and root.val == targetSum:
        return True

    # Subtract current node's value from the sum we need to reach
    # In the current recursive stack, the targetSum represents the
    # remaining path sum from current node to leaf node
    targetSum -= root.val

    # Continue traversing our tree and return True if one of the
    # left or right paths returns True
    return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

# Iterative DFS Solution
def hasPathSum(root, targetSum):
    # If we start with an empty Tree, return False
    if not root:
        return False

    # Add starting node of our tree DFS to the stack
    stack = [(root, targetSum)]

    # While we still have paths to explore, continue exploring
    while stack:
        # Get the current root and the targetSum starting at that node
        node, remSum = stack.pop()

        # If the current node is a leaf node and is the remaining number
        # to reach our targetSum, return True
        if not node.left and not node.right and node.val == remSum:
            return True

        # If we have a left child, add it to our exploration nodes with
        # the targetSum starting at that child
        if node.left:
            stack.append((node.left, remSum - node.val))

        # If we have a right child, add it to our exploration nodes with
        # the targetSum starting at that child
        if node.right:
            stack.append((node.right, remSum - node.val))

    # We have explored all paths, return False
    return False