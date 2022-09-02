import collections


def isSameTree(self, p, q):
    # If 'p' and 'q' are both None, they
    # are the same tree
    if not p and not q:
        return True

    # If one of 'p' or 'q' is None, they are
    # different trees
    if not p or not q:
        return False

    # If both 'p' or 'q' exist and their values
    # are different, they are different trees
    if p.val != q.val:
        return False

    # The nodes at p and q are the same, thus check if
    # p and q's left and right children are the same.
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Stack Solution DFS
def isSameTree2(self, p, q):
    stack = [(p, q)]
    while stack:
        node1, node2 = stack.pop()

        # If both are 'None', continue on to next iteration
        if not node1 and not node2:
            continue

        # If both are not 'None' and have the same value, add their children to
        # the stack for evaluation
        if node1 and node2 and node1.val == node2.val:
            # Essentially adding to the stack an array with the tuples of the two node's
            # left and right children
            stack.extend([(node1.left, node2.left), (node1.right, node2.right)])

        # If either both nodes were not 'None' but had different values or
        # if one of the two nodes were 'None', we just return False
        else:
            return False
    return True

# DFS w/ Queue
def isSameTree3(p, q):
    q = collections.deque([(p, q)])
    while q:
        node1, node2 = q.popleft()

        # If both are 'None', continue on to next iteration
        if not node1 and not node2:
            continue

        # If both are not 'None' and have the same value, add their children to
        # the queue for evaluation
        if node1 and node2 and node1.val == node2.val:
            q.append((node1.left, node2.left))
            q.append((node1.right, node2.right))

        # If either both nodes were not 'None' but had different values or
        # if one of the two nodes were 'None', we just return False
        else:
            return False
    return True