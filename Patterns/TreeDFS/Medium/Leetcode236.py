# Recursive Solution
def lowestCommonAncestor(self, root, p, q):
    # If we encounter 'None', we know that we can't find 'p' or 'q' if we search
    # further, so return 'None'
    if not root:
        return None

    # If when looking for 'p' and 'q', the node we are currently at
    # is 'p' or 'q', just return itself
    if root == p or root == q:
        return root

    # Search for 'p' and 'q' in root's left and right subtrees
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    # Analyze Results after we hit the base cases and return upwards

    # If both of current node's children found a node and returned something,
    # the parent is the LCA
    if left and right:
        return root

    # Either one of the children returned a node, meaning either p or q was
    # found on the left or right subtree.
    # Example: if 'p' was found in the left subtree and right returned 'None'. This
    # would mean that 'q' is somewhere below the node where 'p' was found. So when 'p'
    # is found, we do not need to search all the way down, because in this scenario,
    # the node where 'p' is found would be the LCA.
    else:
        return left or right