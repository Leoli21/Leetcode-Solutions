# Iterative Solution
def lowestCommonAncestor(self, root, p, q):
    while root:
        # If the current node's value has a value greater than the
        # larger of the two values, then the lowest common ancestor
        # must lie in the left subtree (We need to search in subtree
        # where values are smaller than root's current value)
        if root.val > max(p.val, q.val):
            root = root.left
        # If the current node's value is smaller than the
        # smaller of the two values, then the lowest common ancestor
        # must lie in the right subtree. (We need to search in subtree
        # where values are larger than current root's value)
        elif root.val < min(p.val, q.val):
            root = root.right

        # Otherwise, we have found the LCA node as this node
        # is the last node before the 'p' and 'q' split into
        # different subtrees
        else:
        # p.val <= root.val <= q.val or q.val <= root.val <= p.val
            return root


# Recursive Solution
def lowestCommonAncestor(self, root, p, q):
    # If both p and q have values less than root, then the
    # lowest common ancestor must be to the left of current node
    if p.val < root.val and q.val < root.val:
        return self.lowestCommonAncestor(root.left, p, q)

    # If both p and q have values greater then root, then the
    # lowest common ancestor must lie to the right of current node
    elif p.val > root.val and q.val > root.val:
        return self.lowestCommonAncestor(root.right, p, q)

    # If neither of the two conditions are passed, then that means
    # we have found a node that is greater than the smaller of the two
    # but also smaller than the greater of the two. The current node is
    # the last node before the 'p' and 'q' split off into separate subtrees
    else:
        return root
