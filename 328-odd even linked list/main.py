class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        head_next = head.next

        previous_node = head
        node = previous_node.next
        odd_not_even = True
        while node is not None:
            odd_not_even = not odd_not_even
            print(odd_not_even)
            print(node.val)
            if node.next is not None:
                next_node = node.next
                previous_node.next = next_node
                previous_node = node
                node = next_node
            else:
                if odd_not_even:
                    previous_node.next = None
                    node.next = head_next
                else:
                    previous_node.next = head_next
                    node.next = None
                node = None
        return head
