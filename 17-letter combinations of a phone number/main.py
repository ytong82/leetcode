class Solution:
    def letterCombinations(self, digits):
        length = len(digits)
        if length == 0:
            return []

        for i in range(length):
            if len(self.__digit_to_letter(digits[i])) == 0:
                return []

        self.res = list()
        self.__letterCombination(digits, "")
        return self.res

    def __letterCombination(self, digits, letters):
        if len(digits) == 0:
            self.res.append(letters)
            return

        for letter in self.__digit_to_letter(digits[0]):
            self.__letterCombination(digits[1:], letters + letter)

    def __digit_to_letter(self, digit):
        if digit == '2':
            return ['a', 'b', 'c']
        elif digit == '3':
            return ['d', 'e', 'f']
        elif digit == '4':
            return ['g', 'h', 'i']
        elif digit == '5':
            return ['j', 'k', 'l']
        elif digit == '6':
            return ['m', 'n', 'o']
        elif digit == '7':
            return ['p', 'q', 'r', 's']
        elif digit == '8':
            return ['t', 'u', 'v']
        elif digit == '9':
            return ['w', 'x', 'y', 'z']
        else:
            return []


digits = "23"
sol = Solution()
print(sol.letterCombinations(digits))
