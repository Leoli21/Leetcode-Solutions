def reorderList(head):
    # Locate mid point of linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half
    prev = None
    curr = slow.next

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    # To split the two lists in to halves since slow ends up being
    # located at the end of the first two linked list. Setting it's
    # next pointer to None breaks it off from the other half.
    slow.next = None

    # Merge two halves
    head1 = head
    head2 = prev

    while head2:
        oldHead1Next = head1.next
        oldHead2Next = head2.next

        head1.next = head2
        head1 = oldHead1Next

        head2.next = head1
        head2 = oldHead2Next
