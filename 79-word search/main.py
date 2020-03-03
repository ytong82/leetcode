class Solution:
    def exist(self, board, str):
        self.height = len(board)
        if self.height == 0:
            return False
        self.width = len(board[0])

        if_exist = False
        for i in range(self.height):
            for j in range(self.width):
                if self.__exist(board, str, i, j):
                   return True

        return False

    def __exist(self, board, str, i, j):
        if i < 0 or i >= self.height or j < 0 or j >= self.width:
            return False

        if board[i][j] == str[0]:
            if len(str) == 1:
                return True
            board[i][j] = 0
            res = self.__exist(board, str[1:], i-1, j) \
                  or self.__exist(board, str[1:], i+1, j) \
                  or self.__exist(board, str[1:], i, j-1) \
                  or self.__exist(board, str[1:], i, j+1)
            if res:
                return True
            else:
                board[i][j] = str[0]
                return False
        else:
            return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]

word = "ABCCED"
word = "SEE"
word = "ABCB"

board = [["a", "a"]]
word = "aaa"

board = [["C","A","A"],["A","A","A"],["B","C","D"]]
word = "AAB"

sol = Solution()
print(sol.exist(board, word))
