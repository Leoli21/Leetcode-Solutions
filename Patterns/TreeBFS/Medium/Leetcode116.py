import collections

# Solution 1: Right to Left BFS
def connect(self, root):
    if not root:
        return root
    q = collections.deque([root])
    nxt = None
    while q:
        # For each level, reset nxt to None, because we are traversing
        # each level in the reverse order (right to left). And initially
        # we want to set the last node of the level to 'None'.
        nxt = None

        # Process the current level
        for i in range(len(q)):
            # Get the current node from queue
            curr = q.popleft()
            # Add the right node before left node to queue because we want to traverse
            # the next level of the tree in reverse order or right to left.
            # Only need to check if it has a right child b/c tree is a perfect bianry tree.
            if curr.right:
                q.extend([curr.right, curr.left])

            # Set the current node's next pointer to it's right neighbor node on same level
            # which is stored in nxt
            curr.next = nxt

            # Update nxt to the current node because we are traversing the level in reverse
            # order.
            nxt = curr

    return root

# Solution 2:
# DFS
def connect(self, root):
    if not root: return None
    # For each node, obtain it's left and right children, and it's next node
    l = root.left
    r = root.right
    nxt = root.next
    # If child node exists, we can populate the next pointers of current subtree
    if l:
        # Set the next of left child to current node's right child
        l.next = r
        # If current node has a next, then set right child to it's next node's left child
        if nxt:
            r.next = nxt.left
        # Perform the same operations on the next row (this current iteration already dealt with current node's
        # subtree)
        self.connect(l)
        self.connect(r)
    return root

# Solution 3:
# BFS (Optimized)
def connect(self, root):
    # Edge Case: number of nodes in tree is 0
    if not root:
        return root

    # Pointer that marks the first node of the next parent level to be traversed
    nextParentLevel = root

    # As long as we have another parent level to traverse after current level.
    # This will terminate on the last level of a tree as there are no more children
    # nodes to process.
    while nextParentLevel.left:
        # Set the current level of parent nodes to traverse to the nextParentLevel before
        # moving it to the next parent level
        currentParent = nextParentLevel
        nextParentLevel = nextParentLevel.left

        # As long as there are more parent nodes in current level, continue
        # processing child nodes
        while currentParent:
            # We can guarantee that the level we are at has a level below it due to
            # the outer while loop condition
            currentParent.left.next = currentParent.right
            if currentParent.next:
                currentParent.right.next = currentParent.next.left
            # Set the parent pointer to the next parent node in current level
            currentParent = currentParent.next
    return root

