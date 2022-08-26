def sortList(self, head):
    if not head or not head.next:
        return head

    # Get the mid point of the current linked list
    # Starting fast at head.next instead of head in the case where we
    # get to a head with only 2 nodes. This prevents an infinite loop
    # from occurring where our result of splitting a 2 nodes results in
    # a 2 node list and 0 node list. This would continue to result in
    # recursive calls on the 2 node list as it will always result in splits
    # of 2 nodes and 0 nodes instead of the 1 node and 1 node split.

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Slow pointer currently on the last element of the
    # first half. So set the secondHead to it's next node
    # to get save the second half of the list.
    secondHead = slow.next

    # Split the list in half
    slow.next = None

    # Recursively call until all nodes are either one node or
    # are None
    left = self.sortList(head)
    right = self.sortList(secondHead)

    # Merge the two given lists in respective recursive call
    return self.merge(left, right)

def merge(l, r):
    dummy = curr = ListNode()
    while l and r:
        if l.val < r.val:
            curr.next = l
            l = l.next
        else:
            curr.next = r
            r = r.next
        curr = curr.next

    curr.next = l or r
    return dummy.next

