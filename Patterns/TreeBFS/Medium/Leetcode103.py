import collections
# Reversing the order in which we append node values to our current level array.
def zigZagLevelOrder(self, root):
    if not root: return []
    q = collections.deque([root])
    res = []
    # If 'zigzag' is an odd number, then append node values in current order (left to right)
    # If 'zigzag' is an even number, then append node values in reverse order(right to left)
    zigzag = 0
    while q:
        current_level = collections.deque()
        for i in range(len(q)):
            node = q.popleft()
            # Odd: so append in not reverse order
            if zigzag % 2 == 0:
                current_level.append(node.val)
            # Even: so append in reverse order
            else:
                current_level.appendleft(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        # Append the array storing the current level's node values
        res.append(current_level)

        # Update 'zigzag' so that it alternates between odd (reverse order) and even (non-reverse order)
        zigzag += 1
    return res


# Reversing the direction of the current level array before appending
# to result array
def zigZagLevelOrder(self, root):
    if not root: return []
    queue = collections.deque([root])
    res = []

    # 1 means in non-reverse order
    # -1 means in reverse order

    # Starts as non-reverse order
    direction = 1
    while queue:
        # Stores the current level's node's values
        curr_level = []
        # Process all nodes in the current level of tree
        for i in range(len(queue)):
            node = queue.popleft()
            curr_level.append(node.val)
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        # if direction is '1', then append in current order (left to right)
        # if direction is '-1', then append in reverse order (right to left)
        res.append(curr_level[::direction])
        # Direction should alternate due to zig zag pattern
        direction *= -1
    return res

