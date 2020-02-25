class Solution(object):
    def numDecodings(self, s):
        length = len(s)
        count = [0] * length

        for index in range(length):
            if index == 0:
                if 1 <= int(s[index]) <= 9:
                    count[index] = 1
                else:
                    return 0
            elif index == 1:
                if 1 <= int(s[index]) <= 9:
                    count[index] = count[index-1]
                if 10 <= int(s[index-1:index+1]) <= 26:
                    count[index] += 1
            else:
                if 1 <= int(s[index]) <= 9:
                    count[index] = count[index-1]
                if 10 <= int(s[index - 1:index + 1]) <= 26:
                    count[index] += count[index-2]

        print(count)
        return count[index]


solution = Solution()
print(solution.numDecodings("10"))
print(solution.numDecodings("110"))
