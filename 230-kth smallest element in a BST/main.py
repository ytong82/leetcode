class Solution:
    def kthSmallest(self, root, k):
        def findNodeCount(root):
           if root is None:
               return 0
           else:
               return findNodeCount(root.left) + findNodeCount(root.right) + 1

        def doKthSmallest(node, k):
            if root is None:
                return None

            left_node_count = findNodeCount(node.left)
            right_node_count = findNodeCount(node.right)

            if k == left_node_count + 1:
                return node.val
            elif k <= left_node_count:
                return doKthSmallest(node.left, k)
            elif k <= left_node_count + right_node_count + 1:
                return doKthSmallest(node.right, k - left_node_count - 1)
            else:
                return None

        return doKthSmallest(root, k)