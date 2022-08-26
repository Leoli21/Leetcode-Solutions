def hasCycle(head):
    fast = head

    while fast and fast.next:
        head = head.next
        fast = fast.next.next

        if head == fast:
            return True

    return False