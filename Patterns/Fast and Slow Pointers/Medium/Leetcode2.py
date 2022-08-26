def addTwoNumbers(l1, l2):
    result = write = ListNode(0)
    carry = 0
    # Checking carry because sum could have an extra
    # carry of one at the end.
    while l1 or l2 or carry:
        # Add the value from l1 if the end of l1 has not been reached
        # yet. Move to next node after obtaining value.
        if l1:
            carry += l1.val
            l1 = l1.next
        # Add the value from l2 if the end of l2 has not been reached
        # yet. Move to next node after obtaining value.
        if l2:
            carry += l2.val
            l2 = l2.next

        # Create a new node with the digit value of (carry % 10) and set
        # it to write node's next, then advance to the next. Carry stores
        # the sum.
        write.next = ListNode(carry % 10)
        write = write.next

        # Updating the carry
        carry //= 10

    # Return dummy head's next node because the dummy head
    # stores a leading 0 instead of the actual beginning
    # of the resulting sum
    return result.next
