import collections

# BFS
def rightSideView(root):
    visibleValues = []
    if not root:
        return visibleValues

    q = collections.deque()
    q.append(root)
    while q:
        # Get the number of nodes in the current level
        # that we need to process
        nodesInCurrentLevel = len(q)
        # This will store the value of each node in the current
        # level
        currNodeVal = None

        # Process each node in the current level
        for i in range(nodesInCurrentLevel):

            # Get node to process
            node = q.popleft()

            # Store the value of current node
            currNodeVal = node.val

            # Check for left children, and add to queue
            if node.left:
                q.append(node.left)

            # Check for right children and add to queue
            if node.right:
                q.append(node.right)

        # At the end of processing the nodes in the current level,
        # 'currNodeVal' ends up storing the last value in the current
        # level (or the rightmost node in current level)
        visibleValues.append(currNodeVal)
    return visibleValues




# BFS
def rightSideView(root):
    res = []
    nextLevel = []
    q = [root]

    # While we have not processed all levels in tree and
    # while we are not given an empty tree at the beginning
    while q and root:
        # For each node in current level
        for node in q:
            # Check if current node has a left child,
            # add them to the nextLevel
            if node.left:
                nextLevel.append(node.left)

            # Check if current node has a right child,
            # add them to the nextLevel
            if node.right:
                nextLevel.append(node.right)

        # 'node' stores the last node in current level (aka the
        # first node we see from the right)
        res.append(node.val)

        # Set the q to the next level that we have to process
        q = nextLevel

        # Reset the array storing nodes for next level
        nextLevel = []

    return res