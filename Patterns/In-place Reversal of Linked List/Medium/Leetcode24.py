def swapPairs(head):
    if not head or not head.next:
        return head

    dummy = prev = ListNode(0, head)
    curr = head

    # Continue traversal as long as we have two nodes to swap
    while curr and curr.next:
        nxt = curr.next
        curr.next = nxt.next
        nxt.next = curr
        prev.next = nxt

        # Update pointers
        prev = curr
        curr = curr.next

    return dummy.next