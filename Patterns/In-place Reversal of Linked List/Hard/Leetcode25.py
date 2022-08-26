def reverseKGroup(head, k):
    dummy = ListNode(0)
    dummy.next = head

    prevGroup = dummy
    while prevGroup:
        node = prevGroup
        count = 0
        # Check whether there exists k nodes to reverse
        while node and count < k:
            node = node.next
            count += 1

        if not node:
            break

        # Now we know we have k nodes, we will start reversal from first node
        prev = None
        curr = prevGroup.next

        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        tail = prevGroup.next
        tail.next = curr
        prevGroup.next = prev
        prevGroup = tail
    return dummy.next