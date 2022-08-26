def isSubtree(root, subRoot):
    if root is None:
        return False

    if isSameTree(root, subRoot):
        return True

    if isSubtree(root.left, subRoot):
        return True

    if isSubtree(root.right, subRoot):
        return True
    return False



def isSameTree(s, t):
    if not s and not t:
        return True

    if not s or not t or s.val!=t.val:
        return False

    return isSameTree(s.left, t.left) and isSameTree(s.right, t.right)
