class Solution:
    def shortestSubarray(self, A, K):
        length = len(A)

        if length == 0:
            return -1
        elif length == 1:
            if A[0] < K:
                return -1
            else:
                return 1

        left = 0
        right = 0
        summ = 0
        minlen = length + 1
        for i in range(length):
            summ += A[i]
            right += 1

            if summ >= K:
                temp_summ = summ
                for j in range(left, right):
                    if temp_summ >= K and left <= j:
                        left = j
                        summ = temp_summ
                    temp_summ -= A[j]

                if minlen > right - left:
                    minlen = right - left

        if minlen == length + 1:
            return -1
        else:
            return minlen

#A = [1, 2]
#K = 4

#A = [2, -1, 2]
#K = 3
#A = [48, 99, 37, 4, -31]
#K = 140
#A = [17, 85, 93, -45, -21]
#K = 150
#A = [84, -37, 32, 40, 95]
#K = 167

#A = [77, 19, 35, 10, -14]
#K = 19

#A = [89, 67, 99, 25, 29]
#K = 166

A = [-28, 81, -20, 28, -29]
K = 89

sol = Solution()
print(sol.shortestSubarray(A, K))
