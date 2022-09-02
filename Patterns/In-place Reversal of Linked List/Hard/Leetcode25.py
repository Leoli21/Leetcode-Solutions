def reverseKGroup(head, k):
    dummy = ListNode(-1, head)
    prevGroup = dummy

    while True:
        # Check that we have 'k' nodes to perform the reversal
        # on 'k' nodes group
        # Start counting on the node before the new group.
        # This means if we have 'k' nodes, the pointer startGroup
        # will actually land on the node right before the next group node
        # or 'None'.
        startGroup = prevGroup
        count = 0

        # As long as the current we end on is not 'None' and count is less than
        # k, we continue counting until one of the conditions renders False.
        while startGroup and count < k:
            startGroup = startGroup.next
            count += 1

        # This is checking whether we broke out of the above while loop due to reaching
        # 'k' nodes or whether we actually just did not have enough nodes to perform the
        # reverse for a 'k' group.
        if not startGroup:
            break

        # 'prev' is set to startGroup.next, which is essentially the node of the next 'k' group
        # or 'None'. This line prevents us from inluding another line to fix the link between
        # the last node of the reversed group to the node of the next group.
        prev = startGroup.next

        # Start reversing from the start of the 'k' group.
        curr = prevGroup.next

        # Perform the reversal 'k' times, where we are essentially changing
        # 'k' links.
        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Fix the remaining links

        # Save the node at the end of the reversed group
        endGroup = prevGroup.next

        # Set the previousGroup node's next to the start of our reversed group.
        prevGroup.next = startGroup

        # Move our pointer pointing to the last node of a reversed group to the
        # new end of the reversed group so that we can perform the next iteration.
        prevGroup = endGroup

    return dummy.next