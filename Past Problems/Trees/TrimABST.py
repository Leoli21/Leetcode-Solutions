def trimBST(root, low, high):
    if root is None:
        return None

    root.left = self.trimBST(root.left, low, high)
    root.right = self.trimBST(root.right, low, high)

    if root.val > high:
        return root.left

    if root.val < low:
        return root.right

    return root

