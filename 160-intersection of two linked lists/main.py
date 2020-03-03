class Solution:
    def getIntersectionNode(self, headA, headB):
        nodeA = headA
        listA_length = 0
        while nodeA is not None:
            listA_length += 1
            nodeA = nodeA.next

        nodeB = headB
        listB_length = 0
        while nodeB is not None:
            listB_length += 1
            nodeB = nodeB.next

        nodeA = headA
        nodeB = headB
        if listA_length > listB_length:
            nodeA = headA
            steps_to_move = listA_length - listB_length
            for i in range(steps_to_move):
                nodeA = nodeA.next
        elif listA_length < listB_length:
            nodeB = headB
            steps_to_move = listB_length - listA_length
            for i in range(steps_to_move):
                nodeB = nodeB.next

        while nodeA is not None and nodeB is not None:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next

        return None
