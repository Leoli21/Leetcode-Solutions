def buildTree(self, preorder, inorder):
    # Node has no more children nodes, so return 'None' as value of node
    if len(inorder) == 0:
        return None

    # Node has only 1 children node, so just return that node
    if len(inorder) == 1:
        return TreeNode(preorder[0])

    rootVal = preorder[0]
    root = TreeNode(rootVal)

    inorderRootValIndex = inorder.index(rootVal)
    # Left subtree values
    leftInorder = inorder[:inorderRootValIndex]

    # Right subtree values
    rightInorder = inorder[inorderRootValIndex + 1:]

    # Remaining possible node values that could be a root in our
    # left subtree for current node
    leftPreorder = preorder[1: len(leftInorder) + 1]

    # Remaining possible node values that could be a root in our
    # right subtree for current node
    rightPreorder = preorder[len(leftPreorder) + 1:]

    root.left = self.buildTree(leftPreorder, leftInorder)
    root.right = self.buildTree(rightPreorder, rightInorder)

    return root

