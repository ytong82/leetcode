class Solution:
    def groupAnagrams(self, strs):
        l = len(strs)
        if l == 0:
            return []

        map = dict()
        for i in range(l):
            key = ''.join(sorted(strs[i]))
            if key in map.keys():
                map[key].append(i)
            else:
                map[key] = [i]

        res = []
        for key in map.keys():
            res.append([strs[k] for k in map[key]])

        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
sol = Solution()
print(sol.groupAnagrams(strs))