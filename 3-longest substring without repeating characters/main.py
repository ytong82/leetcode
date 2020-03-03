class Solution:
    def lengthOfLongestSubstring(self, str):
        length = len(str)
        if length < 2:
            return length

        book = dict()
        left = 0
        right = 0
        res = 0
        for i in range(length):
            right += 1
            if str[i] in book.keys():
                for j in range(left, right):
                    if str[i] == str[j]:
                        left = j + 1
                        break
                    else:
                        del (book[str[j]])
            else:
                book[str[i]] = 1

            if res < right - left:
                res = right - left

        return res


str = "abcabcbb"
str = "bbbbb"
str = "pwwkew"
str = "tmmzuxt"
sol = Solution()
print(sol.lengthOfLongestSubstring(str))