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
        # node in the path by using 0 as leftGain or rightGain
        leftGain = max(getMaxGain(node.left), 0)
        rightGain = max(getMaxGain(node.right), 0)

        # Sum of the path that involves both the current node and the largest left subtree path and right
        # subtree path. It is important to note that this path sum could only contain the node's value if
        # both leftGain and rightGain ended up resulting in a negative value.

        # Thus, currentPathSum really contains the max between the four possible paths:
        # 1. node.val (if both leftGain and rightGain are negatives)
        # 2. node.val + leftGain (if rightGain was negative)
        # 3. node.val + rightGain (if leftGain was negative)
        # 4. node.val + leftGain + rightGain (this occurs when leftGain and rightGain had a positive result)
        currentPathSum = node.val + leftGain + rightGain
        maxPath = max(maxPath, currentPathSum)

        # Returning the largest path sum for current node. This is checking which path (left or right subtree) sum
        # is greater and returning that + current node's val.
        return node.val + max(leftGain, rightGain)

    getMaxGain(root)
    return maxPath
