from collections import defaultdict


def pathSum(self, root, targetSum):
    # Maintain a global variable that keeps count of
    # the total paths that lead to the targetSum
    self.total = 0

    # Dictionary that saves all the previous path sums up
    # to the current node
    self.paths = defaultdict(int)

    def dfs(node, curSum):
        # Exit condition: if we reach 'None'
        if not node:
            return None

        # Update the current sum to include current node
        curSum += node.val

        # Check if the current path from root to current node
        # equals the targetSum
        if curSum == targetSum:
            self.total  += 1

        # Check if there is a path between the root and current node
        # where the pathSum is equal to targetSum
        # Key Idea:
        # If within the current path (root to currentNode), there is a valid path, then there
        # must be a previous path sum where: previousPathSum + targetSum = curSum
        # This expression can be rearranged to: previousPathSum = curSum - targetSum b/c
        # our 'self.paths' dictionary is storing previousPathSums
        self.total += self.paths[curSum - targetSum]

        # Update the dictionary to store the current path sum from root to current node
        self.paths[curSum] += 1

        # DFS on the left and right children
        dfs(node.left, curSum)
        dfs(node.right, curSum)

        # When we move to a different path, the current sum of the path is
        # no longer available.
        self.paths[curSum] -= 1

    dfs(root, 0)
    return self.total
