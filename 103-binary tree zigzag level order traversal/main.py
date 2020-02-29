class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        res = []
        res.append([root.val])

        queue = []
        queue.append(root)

        level_nodes = []
        level_node_count = 1
        next_level_node_count = 0
        left_to_right = True
        while len(queue) > 0:
            node = queue.pop(0)
            level_node_count -= 1
            if node.left is not None:
                level_nodes.append(node.left.val)
                queue.append(node.left)
                next_level_node_count += 1
            if node.right is not None:
                queue.append(node.right)
                level_nodes.append(node.right.val)
                next_level_node_count += 1
            if len(level_nodes) > 0:
                if level_node_count == 0:
                    left_to_right = not left_to_right
                    if left_to_right:
                        res.append(level_nodes)
                    else:
                        res.append(level_nodes[::-1])
                    level_nodes = []
                    level_node_count = next_level_node_count
                    next_level_node_count = 0

        return res