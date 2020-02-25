class Solution(object):
    def __init__(self):
        self.list = []    

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self._generateParenthesis(n, 0, '')
        return self.list
    
    def _generateParenthesis(self, n, m, str):
        if n > 1:
            k = m + 1
            str += '('
            while k >= 0:
                s = m + 1 - k
                if s > 0:
                    str += ')'
                self._generateParenthesis(n - 1, k, str)
                k -= 1
        elif n == 1:
            str += '()'
            k = m
            while k > 0:
                str += ')'
                k -= 1
            self._generateParenthesis(n - 1, k, str)
        elif n == 0:
            self.list.append(str)


if __name__ == '__main__': 
    solution = Solution()
    solution.generateParenthesis(3)

