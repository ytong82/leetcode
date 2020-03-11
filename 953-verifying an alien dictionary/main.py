class Solution:
    def isAlienSorted(self, words, order):
        length = len(words)
        if length == 1:
            return True

        def __makeOrderDict(order):
            orderDict = dict()
            for index in range(26):
                orderDict[order[index]] = index + 1
            return orderDict

        self.orderDict = __makeOrderDict(order)

        def __compareWords(word, word2):
            wordLen = len(word)
            wordLen2 = len(word2)
            index = 0
            while index < wordLen and index < wordLen2:
                if self.orderDict[word[index]] < self.orderDict[word2[index]]:
                    return True
                elif self.orderDict[word[index]] > self.orderDict[word2[index]]:
                    return False
                index += 1

            if wordLen <= wordLen2:
                return True
            else:
                return False

        for index in range(length-1):
            if not __compareWords(words[index], words[index+1]):
                return False

        return True


words = ["hello", "leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

sol = Solution()
print(sol.isAlienSorted(words, order))