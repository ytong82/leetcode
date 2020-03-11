class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def __findPath(root, node, path):
            path.append(root)
            if node.val == root.val:
                return
            elif node.val < root.val:
                __findPath(root.left, node, path)
            else:
                __findPath(root.right, node, path)

        path_p = []
        __findPath(root, p, path_p)

        path_q = []
        __findPath(root, q, path_q)

        index = 0
        len_path_p = len(path_p)
        len_path_q = len(path_q)
        while index < len_path_p - 1 and index < len_path_q - 1:
            if path_p[index+1].val != path_q[index+1].val:
                return path_p[index]
            index += 1

        if len(path_p) <= len(path_q):
            return path_p[-1]
        else:
            return path_q[-1]
