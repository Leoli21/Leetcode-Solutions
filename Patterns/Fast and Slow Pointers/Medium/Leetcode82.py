def deleteDuplicates(head):
    if not head or not head.next:
        return head

    dummy = lastUniqueNode = ListNode(0, head)
    cur = head

    # Continue traversal of list as long as we have a valid node
    # and a neighbor to compare it to
    while cur and cur.next:
        # Check if we have reached a node that has a duplicate
        if cur.val == cur.next.val:
            # Continue traversing the list until we find another node
            # that has a different value from the duplicate value.
            # When we do find one, the 'cur' pointer will have a
            # neighbor node with a different value.
            while cur.next and cur.val == cur.next.val:
                cur = cur.next

            # Set the last unique node's next pointer to the last duplicate
            # node from the duplicate sequence's 'next' b/c it's neighbor is
            # the next unique node.
            lastUniqueNode.next = cur.next

        # If next node is not a duplicate of current, then we can move both our
        # pointers forward for the next comparison.
        else:
            lastUniqueNode = cur

        cur = cur.next

    return dummy.next