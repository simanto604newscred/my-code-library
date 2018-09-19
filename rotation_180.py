class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.rotating_map = {
            '0':'0',
            '1':'1',
            '2':'5',
            '5':'2',
            '8':'8',
            '6':'9',
            '9':'6'
        }
        result = set()

        for digit in range(N+1):
            if digit in result:
                continue
            rotated_dig = self.is_goodable(digit)
            if rotated_dig:
                result.add(digit)
                if rotated_dig < N and rotated_dig not in result:
                    result.add(rotated_dig)
        print(len(result))
        print(result)
        return  len(result)
    def is_goodable(self, digit):
        rotated_digit = []
        for single_digit in list(str(digit)):
            if single_digit in self.rotating_map.keys():
                rotated_digit.append(self.rotating_map[single_digit])
            else:
                return False
        rotated_digit  = int(''.join(rotated_digit))
        if rotated_digit == digit:
                return False
        else:
            return True, rotated_digit


if __name__ == '__main__':
    Solution().rotatedDigits(10000)
