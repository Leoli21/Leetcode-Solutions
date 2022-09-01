import collections


def widthOfBinaryTree(self, root):
    previousLevel, firstNodeInLevel, maxWidth = 1, 1, 0
    q = collections.deque([[root, previousLevel, firstNodeInLevel]])

    while q:
        # Unpack the array in queue
        [node, level, num] = q.popleft()

        # Update our previousLevel when we reach the first node in a new level
        # Also update our firstNodeInLevel to the index number of first node
        # in the new level (This is used for our calculation of maxWidth)
        if level > previousLevel:
            previousLevel = level
            firstNodeInLevel = num

        # num - firstNodeInLevel + 1 (to include the current node
         # in width)
        maxWidth = max(maxWidth, num - firstNodeInLevel + 1)

        # Check if current node has a left child: left child's number is always
        # parentNodeNum * 2
        if node.left:
            q.append([node.left, level + 1, num * 2])

        # Check if current node has a right child: right child's number is always
        # parentNodeNum * 2 + 1
        if node.right:
            q.append([node.right, level + 1, num * 2 + 1])

    return maxWidth
