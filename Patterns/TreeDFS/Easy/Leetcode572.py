def isSubtree(self, root, subRoot):
    # Base Case: if we arrive at a subtree with a root
    # of 'None'
    if not root:
        return False

    # Check if current subtree at 'root' is the same tree as subRoot
    if self.sameTree(root, subRoot):
        return True

    # At this point, we know that the subtree starting at root is not
    # the same tree as subRoot.

    # So we should check if root's left subtree is the same tree as subRoot
    # or if root's right subtree is the same tree as subRoot
    # Essentially, we are checking if subRoot is the same as one of root's
    # subtrees (left or right)
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)



def sameTree(self, m, n):
    if not m and not n:
        return True

    if not m or not n:
        return False

    if m.val != n.val:
        return False

    return self.sameTree(m.left, n.left) and self.sameTree(m.right, n.right)