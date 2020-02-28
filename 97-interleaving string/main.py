class Solution:
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if l1 == l2 == l3 == 0:
            return True

        if l1 == 0:
            return s2 == s3
        if l2 == 0:
            return s1 == s3

        if l1 + l2 != l3:
            return False

        res = [[False for j in range(l2+1)] for i in range(l1+1)]
        res[0][0] = True
        for i in range(l1+1):
            for j in range(l2+1):
                k = i + j
                if i > 0 and res[i-1][j] and s1[i-1] == s3[k-1]:
                    res[i][j] = True
                if j > 0 and res[i][j-1] and s2[j-1] == s3[k-1]:
                    res[i][j] = True
        return res[i][j]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
sol = Solution()
print(sol.isInterleave(s1, s2, s3))