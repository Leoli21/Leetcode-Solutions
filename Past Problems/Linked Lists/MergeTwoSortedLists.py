class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    newHead = ListNode()
    pointer = newHead

    while list1 and list2:
        if list1.val <= list2.val:
            pointer.next = list1
            list1 = list1.next
        else:
            pointer.next = list2
            list2 = list2.next
        pointer = pointer.next

    pointer.next = list1 or list2
    return newHead.next