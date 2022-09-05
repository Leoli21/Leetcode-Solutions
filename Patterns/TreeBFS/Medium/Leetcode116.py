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
    head = root
    while root:
        # Set 'cur' to the first node of the next level and set 'root' to the
        # updated 'cur' left child (which is the next level's first node).
        cur, root = root, root.left
        # While we still have more nodes in current level
        # to process, continue to update the next pointers
        # of 'cur' pointer's children.
        while cur:
            # If there is a level below the current node's level, we
            # can assign the next pointers
            if cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
            # We are currently on the last level of the tree, therefore break.
            else:
                break
            # Set the current pointer to the next node on the current level.
            cur = cur.next
    return head

