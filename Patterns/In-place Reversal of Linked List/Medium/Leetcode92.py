def reverseBetween(head, left, right):
    # if reverse portion contains only one node or list only
    # contains one node, just return the original list
    if left == right or not head.next:
        return head

    # Create a dummy node in case our reverse portion includes the
    # head node
    dummy = prevLeft = ListNode(0, head)
    curr = head

    # 1) Reach node at position "left"
    for i in range(1, left):
        prevLeft = curr
        curr = curr.next

    # Now curr = "left", prevLeft = "node before left" or the node before reverse portion
    # 2) Reverse [left, right] using 3 pointer approach
    prev = None
    for i in range(right - left + 1):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # 3) Updating connections

    # Fix the connections for the end of the reversed list by setting
    # it to the node directly after "right"
    # prevLeft.next is the node at 'left' or the end of the reversed portion
    # This node's 'next' is current set to None.
    prevLeft.next.next = curr # curr is the node directly after "right"

    # Fix the connection for the start of the reversed list by connecting
    # it to the nodes before "left"
    # prevLeft.next is current set to the node at the end of the reversed list portion
    prevLeft.next = prev # prev is at the "right" node

    return dummy.next