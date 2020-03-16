class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def traverseToFindPath(root, p, q, path, ppath, qpath):
            if root is None:
                return
            else:
                path.append(root)
                if root == p:
                    for pa in path:
                        ppath.append(pa)

                elif root == q:
                    for pa in path:
                        qpath.append(pa)

                if len(ppath) == 0 or len(qpath) == 0:
                    traverseToFindPath(root.left, p, q, path, ppath, qpath)
                    traverseToFindPath(root.right, p, q, path, ppath, qpath)

                path.pop()

        path = []
        ppath = []
        qpath = []

        traverseToFindPath(root, p, q, path, ppath, qpath)

        plen = len(ppath)
        qlen = len(qpath)

        if plen == 0 or qlen == 0:
            return None

        length = min(plen, qlen)

        lcs = ppath[0]
        for i in range(length):
            if ppath[i] == qpath[i]:
                lcs = ppath[i]
            else:
                break

        return lcs