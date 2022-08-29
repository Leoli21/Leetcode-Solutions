def diameterOfBinaryTree(self, root):
    self.diameter = 1

    def depth(root):
        # Base Case: we have reached a 'None' node
        if not root:
            return 0

        # Calculate the height of the left and right subtree for current
        # 'root'
        lHeight = depth(root.left)
        rHeight = depth(root.right)

        # Update the max diameter by comparing the current longest
        # diameter encountered and the current calculated diameter
        # which is the diameter
        self.diameter = max(self.diameter, 1 + lHeight + rHeight)

        # Returning the greatest depth from current node to a leaf node;
        # Adding 1 to include current node to that height
        return 1 + max(lHeight, rHeight)

    depth(root)
    # Subtract by 1 because the number of edges in a path
    # is equal to: # of nodes - 1
    return self.diameter - 1