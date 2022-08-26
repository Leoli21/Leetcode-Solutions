def rotateRight(head, k):
    # Edge Cases:
    # 1. 0 nodes results in no rotations
    # 2. 1 node results in the same node after 'k' rotations
    if not head or not head.next:
        return head

    # Count number of nodes linked list contains
    length = 1
    cur = head
    while cur.next:
        cur = cur.next
        length += 1

    k %= length
    # Edge Case: k == length meaning we end up
    # with the same list after 'k' rotations
    # 'k' would end up equal to 0 if this above is True

    if not k:
        return head

    # Perform 'k' rotations
    curr = head

    # Get to node before split
    for i in range(1, length - k):
        curr = curr.next

    newHead = curr.next
    # Split the list
    curr.next = None

    # Connect the second half to the original first half (head)
    # Since the previous pointer used to count the number of nodes
    # in our list ends up lying at the end of our new head (cur)
    cur.next = head

    return newHead