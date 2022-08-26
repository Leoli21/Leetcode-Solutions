def removeElements(head, val):
    dummy = ListNode(-1, head)
    prevNode = dummy

    while head:
        if head.val == val:
            prevNode.next = head.next
        else:
            prevNode = prevNode.next
        head = head.next
    return dummy.next