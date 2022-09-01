def isValidBst(self, root):
    def helper(node, lower, upper):
        # Empty node or empty tree
        if not node:
            return True

        # Check that node falls in the range (lower, upper)
        if lower < node.val < upper:

            # Check if node's children also fall in their respective ranges with the folloinwg
            # updates to range:
            # Left Child
            # Everything in left subtree of node should be less than current node.val but greater than
            # original lower

            # Right Child
            # Everything in right subtree of current node should be greater than current node.val but less
            # than the original upper
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        # Node does not lie in the range, thus early termination
        else:
            return False

    return helper(root, float('-inf'), float('inf'))