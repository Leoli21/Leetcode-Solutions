def removeNthFromEnd(head, n):
    slow = fast = head
    for i in range(n):
        fast = fast.next

    # If fast is already None, it means we have
    # to delete the head itself. So just return head's
    # next node.
    if not fast:
        return head.next

    # Iterate until fast reaches the last node of the list
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Removing the nth node from end of list
    slow.next = slow.next.next
    return head
