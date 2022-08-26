def reverseKGroup(head, k):
    dummy = ListNode(-1, head)
    prevGroup = dummy

    while True:
        startGroup = prevGroup
        count = 0
        while startGroup and count < k:
            startGroup = startGroup.next
            count += 1

        if not startGroup:
            break

        prev = startGroup.next
        curr = prevGroup.next

        for i in range(k):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        endGroup = prevGroup.next
        prevGroup.next = startGroup
        prevGroup = endGroup

    return dummy.next