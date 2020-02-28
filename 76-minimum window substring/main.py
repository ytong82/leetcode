import collections
import math

class Solution(object):
    def minWindow(self, s, t):
        ls = len(s)
        lt = len(t)

        if ls < lt:
            return ""

        book = self.hashIt(t)
        left = 0
        right = 0
        sws = [math.inf, 0, 0]
        for i in range(ls):
            if s[i] in book.keys():
                book[s[i]] -= 1

            for j in range(left, right):
                if s[j] in book.keys():
                    if book[s[j]] < 0:
                        left += 1
                        book[s[j]] += 1
                    else:
                        break
                else:
                    left += 1

            right += 1
            if self.ifValidWindow(book):
                ws = right - left
                if sws[0] > ws:
                    sws = [ws, left, right]

        return s[sws[1]:sws[2]]


    def ifValidWindow(self, book):
        for k in book.keys():
            if book[k] > 0:
                return False
        return True


    def hashIt(self, t):
        return dict(collections.Counter(t))


S = "ADOBECODEBANC"
T = "ABC"
S = "abc"
T = "cba"
sol = Solution()
print(sol.minWindow(S, T))