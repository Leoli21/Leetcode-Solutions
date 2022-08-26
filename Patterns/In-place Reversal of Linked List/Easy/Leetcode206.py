def reverseList(head):
    # Iterative Solution
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev

def reverseList(head):
    # Recursive Solution
    if not head or not head.next:
        return head

    # Serves as the new head of the reversed list
    reversedListHead = self.reverseList(head.next)
    # Make the next node of the current node point to the
    # current node
    head.next.next = head

    # Helps us remove the cycle which is formed for each
    # call stack. For the last call stack, it sets the last
    # node of the reversed linked list to 'None'. Essentially
    # this line helps clear any possible cycle in the new linked list
    head.next = None
    return reversedListHead