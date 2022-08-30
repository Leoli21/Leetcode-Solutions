
# Recursive
def kthSmallest(self, root, k):
    self.k = k
    self.res = None
    self.inOrder(root)
    return self.res

def inOrder(self, node):
    if not node:
        return

    self.inOrder(node.left)
    self.k -= 1
    if self.k == 0:
        self.res = node.val
        return
    self.inOrder(node.right)

# Iterative
def kthSmallest(self, root, k):
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right