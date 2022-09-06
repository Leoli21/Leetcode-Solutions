# BFS Level Order Traversal Solution #1

def connect(self, root):
    # Create a node that will traverse the tree
    node = root

    # tail is essentially traversing the children level of parent node
    dummy = tail = Node(0)
    while node:
        # Processing current subtree's 'next' pointers

        tail.next = node.left
        if tail.next:
            tail = tail.next

        tail.next = node.right
        if tail.next:
            tail = tail.next

        # Finished setting next pointers for current subtree, move to next
        # subtree
        node = node.next

        # No more parent elements in current level, thus reset tail
        # back to 'dummy' for next level traversal (if we leave it there,
        # the last child of the previous level will point to another node instead
        # of 'None'.
        # Move 'node' to dummy's next because dummy's next was previously set to the
        # first child of the previous level's first child.
        if not node:
            tail = dummy
            node = dummy.next
    return root

# BFS Level Order Traversal Solution #2
def connect(self, root):
    node = root
    while node:
        cur = dummy = Node(0)
        # While there still exists parent nodes to evaluate, perform the
        # following on the children:
        # For current parent:
        # Check if left child exists set dummy's next to left child, so that
        # for when we finish the current level, our new traversal for parent begins
        # at dummy's next.
        # Check if right child exists and connect left and right children.
        while node:
            if node.left:
                cur.next = node.left
                cur = cur.next

            if node.right:
                cur.next = node.right
                cur = cur.next

            # After processing node's left and right children, move to next parent node
            # in level.
            node = node.next

        # Move to next level so that parent level is now the fully processed children level.
        # If we just processed the last row in tree, this will be None.
        node = dummy.next
    return root