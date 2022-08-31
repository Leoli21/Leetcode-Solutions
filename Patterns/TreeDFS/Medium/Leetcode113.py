def pathSum(self, root, targetSum):
    res = []
    self.dfs(root, targetSum, [], res)
    return res

# Function that traverses a tree through DFS
def dfs(self, cur, targetSum, curRes, res):
    # We have reached a 'None' node
    if not cur:
        return

    # Reached a leaf node, check if the path
    # leads to the targetSum
    if not cur.left and not cur.right and cur.val == targetSum:
        # Add the current value to our result array before adding
        # it to our answer array
        curRes.append(cur.val)
        res.append(curRes)

    # Continue traversing the tree through the left and right
    # until we reach a leaf node
    # Make sure to update the targetSum and add the current node
    # before moving to the left and right children
    self.dfs(cur.left, targetSum - cur.val, curRes + [cur.val], res)
    self.dfs(cur.right, targetSum - cur.val, curRes + [cur.val], res)


