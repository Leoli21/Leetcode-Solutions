def isSameTree(p, q):
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