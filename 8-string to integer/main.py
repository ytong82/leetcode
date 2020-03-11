import string


class Solution:
    def myAtoi(self, str):
        valid = False
        sign = None

        length = len(str)

        left = 0
        right = 0
        index = 0
        for s in str:
            if valid:
                if s in string.digits:
                    right += 1
                else:
                    break
            else:
                if s in string.digits:
                    valid = True
                    left = index
                    right = left

                if s not in string.whitespace \
                        and s not in string.digits \
                        and s not in ['+', '-']:
                    return 0

                if s in ['+', '-']:
                    if sign is None:
                        if s == '-':
                            sign = False
                        else:
                            sign = True
                    else:
                        return 0

                    if index + 1 < length \
                        and str[index+1] not in string.digits:
                        return 0

            index += 1

        if valid:
            to_number = str[left:right+1]
            if len(to_number) == 0:
                return 0
            number = int(to_number)
            MAX_INT = pow(2, 31) - 1
            MIN_INT = - pow(2, 31)
            if sign is None:
                sign = True
            if sign:
                if number <= MAX_INT:
                    return number
                else:
                    return MAX_INT
            else:
                number = 0 - number
                if number >= MIN_INT:
                    return number
                else:
                    return MIN_INT
        else:
            return 0


#str = "42"
#str = "-42"
#str = "4193 with words"
#str = "words and 987"
#str = "-91283472332"
#str = ".1"
#str = "+"
#str = "+-2"
#str = "-   234"

sol = Solution()
print(sol.myAtoi(str))