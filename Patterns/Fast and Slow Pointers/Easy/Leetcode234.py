def isPalindrome(head):
    fast = slow = head
    # Find middle node using Floyd's: By the time
    # the fast pointer reaches the end, the slow pointer
    # should reach the middle b/c fast pointer travels
    # two times as fast as the slow pointer.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the linked list

    # Have the second half of the linked list end at 'None'
    # so that we can have a termination when comparing the
    # two later.
    slowsNewNext = None
    while slow:
        # Temp variable that stores slow's right-next node
        next = slow.next

        # Set the next pointer of slow to the previous node
        # (This step is essentially setting slow's next pointer to
        # the node to its left)
        slow.next = slowsNewNext

        # Set up the next reversal of next pointer for next iteration
        slowsNewNext = slow

        # Moving slow pointer to it's next node (right node)
        slow = next

    # Compare first half of list and the reversed second
    # half of the list

    # Eventually slowsNewNext will reach a 'None' node, leading
    # to termination (signalling the end of the palindrome)
    while slowsNewNext:
        if slowsNewNext.val != head.val:
            return False
        slowsNewNext = slowsNewNext.next
        head = head.next
    return True
