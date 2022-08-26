def preorder(self, root):
    # Recursive Approach
    res = []
    self.dfs(root, res)
    return res

    def dfs(self, root, res):
        if root is None:
            return None

        res.append(root.val)

        for children in root.children:
            self.dfs(children, res)

    # Iterative Approach w/ Stack
def preorder(self, root):
    if root is None:
        return []

    stack = [root]
    res = []
    while stack:
        temp = stack.pop()
        res.append(temp.val)
        stack.extend(temp.children[::-1])
