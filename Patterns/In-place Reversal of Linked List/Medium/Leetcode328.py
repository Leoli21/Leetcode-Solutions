def oddEvenList(head):
    # Edge Cases:
    # 1. If 0 nodes, return head
    # 2. If 1 node, return head
    # 3. if 2 nodes, return head since list will already be in odd-even
    if not head or not head.next or not head.next.next:
        return head

    # Pointer that keeps track of current odd nodes and acts as
    # the tail for the odd indexed linked list
    odd = head

    # Pointer for even indexed list and head for even indexed list
    even = evenHead = head.next

    # Terminate traversal when even is None (for odd number of nodes in list)
    # or has no next node (for even number of nodes in list)
    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next

    odd.next = evenHead
    return head