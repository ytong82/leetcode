class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return head

        dummy = ListNode(None)
        dummy.next = None

        real = dummy
        previous = dummy
        current = head

        while current is not None and current.next is not None:
            if previous.val != current.val and current.val != current.next.val:
                real.next = current
                real = real.next

            previous = current
            current = current.next

        if current.next is None:
            if previous.val != current.val:
                real.next = current
            else:
                real.next = None

        return dummy.next