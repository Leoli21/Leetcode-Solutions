def maxPathSum(self, root):
    # Placeholder
    maxPath = float('-inf')

    def getMaxGain(node):
        # Global variable: 'maxPath'
        nonlocal maxPath
        # We cannot possibly get any gains from a 'None' node
        if node is None:
            return 0

        # In the case that when we look at the left and right branches of current node,
        # we end up with gains less than 0, there is no point in exploring those branches at all

        # The case where this would occur is if the left and right branches were negative numbers.
        # We would then just not even consider adding them to our path and only include our current
        # node in the path
        leftGain = max(getMaxGain(node.left), 0)
        rightGain = max(getMaxGain(node.right), 0)

        # Sum of the path that involves SPLITTING
        currentPathSum = node.val + leftGain + rightGain
        maxPath = max(maxPath, currentPathSum)

        # Returning the path that does NOT involve splitting
        return node.val + max(leftGain, rightGain)

    getMaxGain(root)
    return maxPath
