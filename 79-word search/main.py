import copy

class Solution:
    def exist(self, board, str):
        self.height = len(board)
        if self.height == 0:
            return False
        self.width = len(board[0])

        book = [[0 for i in range(self.width)] for j in range(self.height)]

        if_exist = False
        for i in range(self.height):
            for j in range(self.width):
                if_exist = self.__exist(board, str, i, j, copy.deepcopy(book))
                if if_exist:
                    return if_exist

        return if_exist

    def __exist(self, board, str, i, j, book):
        book[i][j] = 1
        if board[i][j] == str[0]:
            if len(str) == 1:
                return True
            else:
                if i > 0:
                    if book[i-1][j] == 0:
                        if self.__exist(board, str[1:], i-1, j, copy.deepcopy(book)):
                            return True
                if i < self.height - 1:
                    if book[i+1][j] == 0:
                        if self.__exist(board, str[1:], i+1, j, copy.deepcopy(book)):
                            return True
                if j > 0:
                    if book[i][j-1] == 0:
                        if self.__exist(board, str[1:], i, j-1, copy.deepcopy(book)):
                            return True
                if j < self.width - 1:
                    if book[i][j+1] == 0:
                        if self.__exist(board, str[1:], i, j+1, copy.deepcopy(book)):
                            return True
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

sol = Solution()
print(sol.exist(board, word))
