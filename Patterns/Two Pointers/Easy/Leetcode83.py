def deleteDuplicates(head):
    # If linked list contains only one node or is empty, just
    # return itself
    if not head or head.next == None:
        return head

    currNode = head

    # Continue traversing linked list if pointer is not 'None'
    while currNode:

        # First check that the node at pointer has a next node to even compare with it.
        # If it has a next node, check if they have equal values.
        if currNode.next and currNode.val == currNode.next.val:

            # Remove the duplicate value by assigning current node's next pointer to the next
            # node's next node. This skips the next node and removes it from the linked list.
            currNode.next = currNode.next.next

        # Scenario 1: Moving curent node to 'None' node, thus leading to termination of while loop
        # Scneario 2: Moving current node to next node b/c the value at current node and it's next
        # node are not equal.
        else:
            currNode = currNode.next

    # return the head node which contains all the changes that were mode from pointer
    return head