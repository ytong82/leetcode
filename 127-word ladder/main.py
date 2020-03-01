from collections import Counter
import string


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        word_dict = dict(Counter(wordList))
        queue = list()
        queue.append(beginWord)

        word_length = len(beginWord)
        search_length = 1
        level_node_length = 1
        next_level_node_length = 0
        while len(queue) > 0:
            word_node = queue.pop(0)
            level_node_length -= 1

            for index in range(word_length):
                for char in string.ascii_lowercase:
                    if word_node[index] == char:
                        continue
                    else:
                        search_word = word_node[0:index] + char + word_node[index+1:]
                        if search_word == endWord:
                            return search_length + 1
                        if search_word in word_dict.keys() and word_dict[search_word] > 0:
                            word_dict[search_word] -= 1
                            next_level_node_length += 1
                            queue.append(search_word)

            if level_node_length == 0:
                level_node_length = next_level_node_length
                next_level_node_length = 0
                search_length += 1
        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))
