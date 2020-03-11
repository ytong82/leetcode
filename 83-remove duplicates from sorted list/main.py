class Solution:
    def deleteDuplicates(self, head):
        current = head
        anchor = head

        if head is None:
            return head

        while current.next is not None:
            current = current.next
            if anchor.val != current.val:
                anchor.next = current
                anchor = current

        anchor.next = None
        return head
