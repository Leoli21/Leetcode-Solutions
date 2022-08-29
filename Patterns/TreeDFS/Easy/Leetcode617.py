def mergeTrees(root1, root2):
    # If both trees contain a valid node, execute the following
    if root1 and root2:
        # Create a new node with the sum of the two tree's node's values.
        newNode = TreeNode(root1.val + root2.val)

        # Set the left and right children of the current new node
        newNode.left = self.mergeTrees(root1.left, root2.left)
        newNode.right = self.mergeTrees(root1.right, root2.right)

        return newNode

    # If only one of the tree's have a value, then return
    # that one.
    # If both are 'None', 'None will be returned
    else:
        return root1 or root2