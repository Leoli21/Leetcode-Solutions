def hasCycle(head):
    # In the case of 0 Nodes, it is not possible for there to exist a cycle
    if not head:
         return False

    # Two pointers (slow, fast) start at beginning of the linked list
    slow = fast = head

    # Traverse the linked list as long as the fast pointer does not equal 'None' and it has a next node
    # to go to. The fast pointer needs a next node in order for it to jump 2 times (even if the next Node's
    # next pointer points to a 'None' node

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        # If the slow and fast pointer ever land on the same node, there must exist a cycle within the
        # linked list. It would not be possible otherwise for the slow and fast pointers to meet at the
        # exact same node.
        if slow == fast:
            return True

    # Broke out of the while loop traversal. This means that there was a Node in the linked list that
    # pointed to 'None'. In other words, there was a termination point in the linked list (no continuous
    # cycle exists).
    return False
